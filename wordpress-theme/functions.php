<?php
/**
 * The Wall Street Coach functions and definitions
 */

function twsc_setup() {
    // Add support for document title tag
    add_theme_support( 'title-tag' );

    // Add support for post thumbnails
    add_theme_support( 'post-thumbnails' );

    // Register Navigation Menus
    register_nav_menus( array(
        'primary' => __( 'Primary Menu', 'twsc' ),
        'footer'  => __( 'Footer Menu', 'twsc' ),
    ) );
}
add_action( 'after_setup_theme', 'twsc_setup' );

function twsc_add_menu_link_class( $atts, $item, $args ) {
    if ( property_exists($args, 'theme_location') && $args->theme_location == 'primary' ) {
        $atts['class'] = 'nav-link';
    }
    return $atts;
}
add_filter( 'nav_menu_link_attributes', 'twsc_add_menu_link_class', 1, 3 );

function twsc_scripts() {
    // Enqueue Google Fonts
    wp_enqueue_style( 'twsc-google-fonts', 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap', array(), null );

    // Enqueue Main Styles
    wp_enqueue_style( 'twsc-style', get_template_directory_uri() . '/assets/css/styles.css', array(), '4.0' );
    wp_enqueue_style( 'twsc-style-enhanced', get_template_directory_uri() . '/assets/css/styles-enhanced.css', array('twsc-style'), '1.0' );

    // Enqueue Scripts
    wp_enqueue_script( 'twsc-script', get_template_directory_uri() . '/assets/js/script.js', array(), '1.8', true );
}
add_action( 'wp_enqueue_scripts', 'twsc_scripts' );

/**
 * GLOBAL FIX: Force "Resources" menu item to "Tools"
 * ensuring consistency even if page template isn't updated manualy
 */
function twsc_force_tools_menu_item( $items, $args ) {
    if ( isset($args->theme_location) && $args->theme_location == 'primary' ) {
        foreach ( $items as $item ) {
            // Check for "Resources" in title or URL
            if ( stripos( $item->title, 'Resources' ) !== false || stripos( $item->url, 'page-resources' ) !== false || stripos( $item->url, '/resources' ) !== false ) {
                $item->title = 'Tools';
                $item->url = site_url('/tools');
            }
        }
    }
    return $items;
}
add_filter( 'wp_nav_menu_objects', 'twsc_force_tools_menu_item', 1000, 2 );
