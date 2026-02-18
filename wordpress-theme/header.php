<!DOCTYPE html>
<html <?php language_attributes(); ?>>

<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description"
        content="The Wall Street Coach provides neuro-biological performance coaching for professional traders and financial executives. Optimize your psychology and increase your alpha.">
    <meta name="theme-color" content="#1A2A3A">

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VQ84F8PKQ6"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'G-VQ84F8PKQ6');
    </script>

    <!-- FG Funnels Tracking -->
    <script src="https://link.fgfunnels.com/js/external-tracking.js"
        data-tracking-id="tk_9a5af49d48914cadbd326dc070b23e25"></script>

    <?php wp_head(); ?>
    <style>
        @media (max-width: 768px) {
            .nav-logo {
                flex: 0 1 auto !important;
                max-width: 80% !important;
                /* Maximized width for logo */
                margin-right: auto !important;
                min-width: 0 !important;
            }

            .logo-img {
                height: 30px !important;
                width: auto !important;
                max-width: 100% !important;
                object-fit: contain !important;
            }

            .mobile-menu-toggle {
                display: flex !important;
                flex-shrink: 0 !important;
            }

            .nav-tagline {
                display: none !important;
                /* Hide tagline on mobile */
            }
        }

        /* Critical Tagline Styles to bypass cache */
        .nav-tagline {
            display: block !important;
            color: rgba(255, 255, 255, 0.8) !important;
            font-size: 0.65rem !important;
            font-family: 'Space Mono', monospace, sans-serif !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            margin-top: 4px !important;
            line-height: 1.2 !important;
            margin-left: 4px !important;
            /* Optical alignment adjustment */
        }
    </style>
</head>

<body <?php body_class(); ?>>
    <div class="scroll-progress" id="scrollProgress"></div>
    <!-- Global Navigation -->
    <nav class="nav-bar" id="mainNav">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="<?php echo home_url(); ?>"><img
                        src="<?php echo get_template_directory_uri(); ?>/assets/images/The-Wall-Street-Coach-Logo-Transparent@white.png"
                        alt="The Wall Street Coach" class="logo-img"></a>
                <span class="nav-tagline">Transforming Traders from the Inside Out</span>
            </div>
            <button class="mobile-menu-toggle" id="mobileMenuToggle">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul id="navLinks" class="nav-links">
                <li><a href="<?php echo site_url('/assessment'); ?>" class="nav-link">Assessment</a></li>
                <li><a href="<?php echo site_url('/results'); ?>" class="nav-link">Results</a></li>
                <li><a href="<?php echo site_url('/about'); ?>" class="nav-link">About</a></li>
                <li><a href="<?php echo site_url('/coaching'); ?>" class="nav-link">Coaching</a></li>
                <li><a href="<?php echo site_url('/podcasts'); ?>" class="nav-link">Podcast</a></li>
                <li><a href="<?php echo site_url('/tools'); ?>" class="nav-link">Tools</a></li>
            </ul>
        </div>
    </nav>