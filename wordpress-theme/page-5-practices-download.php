<?php
/**
 * Template Name: 5 Practices Download (Thank You)
 */

get_header();
?>

<section class="section" style="padding-top: 150px; min-height: 80vh; display: flex; align-items: center; text-align: center;">
    <div class="container">
        <div style="max-width: 800px; margin: 0 auto;">
            <div style="margin-bottom: 2rem;">
                <!-- Optional: Reuse the check icon or similar -->
                <div style="width: 80px; height: 80px; background: rgba(16, 185, 129, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 2rem;">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                </div>
                
                <h1 style="color: var(--navy); margin-bottom: 1.5rem;">Access Granted!</h1>
                <p class="section-intro" style="margin-bottom: 2rem;">
                    Thank you for requesting <strong>The 5 Practices to Become a Better Trader</strong>.<br>
                    Your copy is ready for immediate download below.
                </p>
            </div>

            <div style="background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); display: inline-block; border: 1px solid rgba(0,0,0,0.05); width: 100%; max-width: 500px;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/5-practices-cover.jpg" alt="Book Cover" style="width: 100%; height: auto; margin-bottom: 2rem; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
                
                <br>

                <a href="<?php echo get_template_directory_uri(); ?>/assets/downloads/The-5-Practices.pdf" download class="btn-primary" style="display: block; width: 100%; padding: 1.25rem 1rem; font-size: 1.1rem; background-color: #08333A !important; color: #C9A227 !important; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;">
                    Download PDF Now
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C9A227" stroke-width="2" style="margin-left: 8px; vertical-align: text-bottom;">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                </a>
                
                <p style="margin-top: 2rem; font-size: 0.9rem; color: var(--text-secondary);">
                    <em>Link will also be sent to your email inbox shortly.</em>
                </p>
            </div>
        </div>
    </div>
</section>

<?php get_footer(); ?>
