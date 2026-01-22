<?php
/**
 * Template Name: Download Page
 */

get_header();
?>

    <!-- Download Section -->
    <section class="section" style="padding-top: 120px; min-height: 80vh;">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">
                <div style="text-align: center; margin-bottom: 3rem;">
                    <h1 style="color: var(--navy); margin-bottom: 1rem; font-size: 2.5rem;">Stop Sabotaging Your Trades. Start Mastering Your Mind.</h1>
                    <p class="section-intro" style="color: var(--gold); font-family: 'Space Mono', monospace; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;">
                        The 5 Proven Practices Used by Top 1% Traders
                    </p>
                </div>

                <div class="download-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start;">
                    <!-- Left: Book & Copy -->
                    <div>
                        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/5-practices-cover.jpg" alt="The 5 Practices" style="width: 100%; max-width: 350px; display: block; margin: 0 auto 2rem; box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-radius: 8px;">
                        
                        <div style="color: var(--text-primary); margin-bottom: 2rem;">
                            <p>You have the strategy. You know the charts. So why isn't your P&L reflecting your potential?</p>
                            <p>The missing link isn't another indicator—it's your internal operating system.</p>
                            <p>In this exclusive guide, Kim Ann Curtin reveals the <strong>5 Transformational Practices</strong> that separate elite market performers from the rest.</p>
                            
                            <h4 style="color: var(--navy); margin-top: 1.5rem;">Featuring Insights From:</h4>
                            <ul class="check-list" style="margin-bottom: 1.5rem;">
                                <li><strong>Jack Kellogg</strong> on Avoiding Destruction</li>
                                <li><strong>Jason Shapiro</strong> on Finding Solutions over Excuses</li>
                                <li><strong>Kyle Williams</strong> on Extreme Ownership</li>
                            </ul>
                            
                            <p>Don't let your psychology be the bottleneck to your financial freedom.</p>
                        </div>
                    </div>

                    <!-- Right: Form -->
                    <div>
                        <div style="background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05);">
                            <h3 style="text-align: center; color: var(--navy); margin-bottom: 1.5rem;">Download Your Free Copy</h3>
                            <div class="form-container-wrapper">
                                <iframe
                                    src="https://link.fgfunnels.com/widget/form/P4QzMatpx421RnihwZsq"
                                    style="width:100%;height:100%;border:none;border-radius:4px"
                                    id="inline-P4QzMatpx421RnihwZsq" 
                                    data-layout="{'id':'INLINE'}"
                                    data-trigger-type="alwaysShow"
                                    data-trigger-value=""
                                    data-activation-type="alwaysActivated"
                                    data-activation-value=""
                                    data-deactivation-type="neverDeactivate"
                                    data-deactivation-value=""
                                    data-form-name="5 Practices - Sign Up (2026)"
                                    data-height="550"
                                    data-layout-iframe-id="inline-P4QzMatpx421RnihwZsq"
                                    data-form-id="P4QzMatpx421RnihwZsq"
                                    title="5 Practices - Sign Up (2026)"
                                        >
                                </iframe>
                                <script src="https://link.fgfunnels.com/js/form_embed.js"></script>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Responsive Styles -->
            <style>
                .form-container-wrapper {
                    width: 100%;
                    min-height: 550px; /* Compact on desktop */
                }

                @media (max-width: 768px) {
                    .download-grid {
                        grid-template-columns: 1fr !important;
                        gap: 3rem !important;
                    }
                    .form-container-wrapper {
                        min-height: 900px !important; /* Tall on mobile */
                    }
                }
            </style>
        </div>
    </section>

<?php get_footer(); ?>
