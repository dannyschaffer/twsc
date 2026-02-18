<?php
/**
 * The Wall Street Coach functions and definitions
 */

function twsc_setup()
{
    // Add support for document title tag
    add_theme_support('title-tag');

    // Add support for post thumbnails
    add_theme_support('post-thumbnails');

    // Register Navigation Menus
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'twsc'),
        'footer' => __('Footer Menu', 'twsc'),
    ));
}
add_action('after_setup_theme', 'twsc_setup');

function twsc_add_menu_link_class($atts, $item, $args)
{
    if (property_exists($args, 'theme_location') && $args->theme_location == 'primary') {
        $atts['class'] = 'nav-link';
    }
    return $atts;
}
add_filter('nav_menu_link_attributes', 'twsc_add_menu_link_class', 1, 3);

function twsc_scripts()
{
    // Enqueue Google Fonts
    wp_enqueue_style('twsc-google-fonts', 'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap', array(), null);

    // Enqueue Main Styles
    wp_enqueue_style('twsc-style', get_template_directory_uri() . '/assets/css/styles.css', array(), '4.0');
    wp_enqueue_style('twsc-style-enhanced', get_template_directory_uri() . '/assets/css/styles-enhanced.css', array('twsc-style'), '1.0');

    // Enqueue Scripts
    // Use time() for version to force cache clearing during debug
    wp_enqueue_script('twsc-script', get_template_directory_uri() . '/assets/js/script.js', array(), time(), true);
}
add_action('wp_enqueue_scripts', 'twsc_scripts');

/**
 * GLOBAL FIX: Force "Resources" menu item to "Tools"
 * AGGRESSIVE MODE: Runs on all menus, no location check
 */
function twsc_force_tools_menu_item($items, $args)
{
    // Run on ALL menus to be safe
    foreach ($items as $item) {
        // Check for "Resources" in title (case insensitive)
        if (stripos($item->title, 'Resources') !== false) {
            $item->title = 'Tools';
            $item->url = site_url('/tools');
        }
        // Check for "resources" in URL
        elseif (stripos($item->url, 'page-resources') !== false || stripos($item->url, '/resources') !== false) {
            $item->title = 'Tools';
            $item->url = site_url('/tools');
        }
    }
    return $items;
}
add_filter('wp_nav_menu_objects', 'twsc_force_tools_menu_item', PHP_INT_MAX, 2);

/**
 * Handle Custom Redirects
 * Specifically for /twsc-podcast/ and /testimonies/ which might not be caught by WP Pages
 */
function twsc_custom_redirects()
{
    $path = trim(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');

    // Map of old slug => new destination (relative to site_url)
    $redirects = [
        'twsc-podcast' => '/podcasts', // Correct page-podcast.php usually maps to /podcasts or /podcast
        'testimonies' => '/results',
        'contact-form' => '/',
        'trader-coaching' => '/coaching',
        'executive-coaching' => '/coaching',
        'coaching-for-executives' => '/coaching',
        'coaching-for-everyone' => '/coaching',
        'about-kim-ann-curtin' => '/about',
        'privacy-policy' => '/privacy-policy',
        'terms-and-conditions' => '/privacy-policy',
        // Specific Episode Fixes
        'blog/2022/11/jack-kellogg' => '/episodes/ep-039-the-wall-street-coach-podcast-interview-with-jack-kellogg.html', // If this is HTML static
        'coaching-for-everyone/contact-coaching-for-everyone' => '/coaching'
    ];

    // Check exact match first
    if (isset($redirects[$path])) {
        wp_redirect(site_url($redirects[$path]), 301);
        exit;
    }

// Check partial matches (e.g. trailing slash logic handled by trim above, but check original if needed)
}
add_action('template_redirect', 'twsc_custom_redirects');