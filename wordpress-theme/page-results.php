<?php
/**
 * Template Name: Results Page
 */

get_header();
?>

<!-- Hero Section -->
<section class="section section-dark" style="padding-top: 6rem; padding-bottom: 4rem;">
    <div class="container" style="text-align: center;">
        <h1 class="hero-headline" style="font-size: 3.5rem; margin-bottom: 1.5rem;">Real Results.<br>Unfakeable Metrics.
        </h1>
        <p class="section-intro" style="max-width: 700px; margin: 0 auto;">
            We don't trade in "feelings." We trade in P&L, Sharpe Ratios, and Drawdown reduction.
            See what happens when you engineer the psychology of a top performer.
        </p>
    </div>
</section>

<!-- Featured Case Study: Metrics -->
<section class="section" style="padding-top: 0; margin-top: -3rem;">
    <div class="container">
        <div class="results-showcase"
            style="background: var(--white); border-radius: 12px; border: 1px solid var(--light-gray); overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <div class="results-grid-layout" style="display: grid; grid-template-columns: 1fr 1fr; gap: 0;">

                <!-- Image Side -->
                <div class="results-image"
                    style="background: #f1f5f9; position: relative; min-height: 400px; display: flex; align-items: center; justify-content: center;">
                    <!-- Using the new image provided by the user -->
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/testimonial 2 2026.png"
                        alt="Significant Trading Performance Metrics"
                        style="width: 100%; height: auto; object-fit: contain; max-height: 500px;">
                </div>

                <!-- Content Side -->
                <div class="results-content"
                    style="padding: 3rem; display: flex; flex-direction: column; justify-content: center;">
                    <span class="segment-label"
                        style="margin-bottom: 1rem; color: var(--gold); border-color: var(--gold); display: inline-block; border-bottom: 2px solid; padding-bottom: 2px;">Featured
                        Case Study</span>
                    <h2 style="color: var(--navy); margin-bottom: 1rem;">The "Perfect" Month</h2>
                    <h3
                        style="font-size: 1.25rem; color: var(--text-secondary); margin-bottom: 2rem; font-family: var(--font-mono);">
                        2026 Performance Metrics</h3>

                    <div class="metrics-grid"
                        style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem;">
                        <div class="metric-item">
                            <span
                                style="display: block; font-size: 2rem; font-weight: 700; color: var(--teal);">95%</span>
                            <span
                                style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Green
                                Days</span>
                        </div>
                        <div class="metric-item">
                            <span
                                style="display: block; font-size: 2rem; font-weight: 700; color: var(--gold);">+14%</span>
                            <span
                                style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Acct
                                Growth YTD</span>
                        </div>
                        <div class="metric-item">
                            <span
                                style="display: block; font-size: 2rem; font-weight: 700; color: var(--navy);">152</span>
                            <span
                                style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Total
                                Trades</span>
                        </div>
                        <div class="metric-item">
                            <span
                                style="display: block; font-size: 2rem; font-weight: 700; color: var(--teal);">67%</span>
                            <span
                                style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-secondary);">Win
                                Rate</span>
                        </div>
                    </div>

                    <p
                        style="font-style: italic; color: var(--text-secondary); border-left: 3px solid var(--gold); padding-left: 1rem;">
                        "Best performance in terms of consistency and calmness."
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Video Case Study -->
<section class="section" style="background: #08333A; color: white;">
    <div class="container">
        <div style="max-width: 900px; margin: 0 auto; text-align: center;">
            <h2 style="color: white; margin-bottom: 2rem;">Inside the Transformation</h2>
            <div style="padding:56.25% 0 0 0;position:relative;">
                <iframe
                    src="https://player.vimeo.com/video/1074435057?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
                    frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media"
                    style="position:absolute;top:0;left:0;width:100%;height:100%; border-radius: 8px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);"
                    title="Client Success Story"></iframe>
            </div>
            <script src="https://player.vimeo.com/api/player.js"></script>
            <p style="margin-top: 2rem; font-size: 1.1rem; opacity: 0.9;">
                Watch how top traders are rewriting their psychological playbook to achieve sustainable success.
            </p>
        </div>
    </div>
</section>

<!-- Testimonials Grid -->
<section class="section" style="background: #f8f9fa;">
    <div class="container">
        <h2 style="text-align: center; margin-bottom: 3rem; color: var(--navy);">What Traders Are Saying</h2>

        <div class="testimonials-grid-layout"
            style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2rem;">

            <!-- Testimonial 1 -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    I pretty much figured I knew everything... I wasn't prepared for the results of the TPI. It gave me
                    real clarity on my biggest hang-ups.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Barry Randall</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">CEO, LSC Investment Group</span>
                </div>
            </div>

            <!-- Testimonial 2 -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    It felt as if Kim lived inside my head... My jaw almost hit the table.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Thuan Q. Pham</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">Former CTO of Uber</span>
                </div>
            </div>

            <!-- Testimonial 3 -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    My win rate improved from 40% to 60% as I began to trade less and make more... The TPI showed me
                    exactly where my issues were stemming from.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Andres A.</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">Independent Trader</span>
                </div>
            </div>

            <!-- Testimonial 4 -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    In just 6 months, I grew my account by over 135%... Far exceeding my prior losses and expectations.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Tom Burnett</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">Trader</span>
                </div>
            </div>

            <!-- Testimonial 5 -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    If you are trading as a professional, it is a MUST do. I cannot thank Kim enough.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Carson Klahm</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">Trader</span>
                </div>
            </div>

            <!-- Testimonial 6 (Longer one) -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    I have been working with Kim for over a year. And I just had my best January since I began trading 5
                    years ago... This has everything to do with trading in peace…trading with neutrality and unattached
                    to the outcome. Kim helped me find this inner peace. Thank you Kim!
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Karim Abdelkader</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">Full Time Trader</span>
                </div>
            </div>

            <!-- Testimonial 7 (From TPI Page) -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    The TPI revealed blind spots I didn't even know I had. My win rate increased 23% in the first month.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Portfolio Manager</strong>
                    <span style="font-size: 0.9rem; color: var(--text-secondary);">Hedge Fund</span>
                </div>
            </div>

            <!-- Testimonial 8 (From TPI Page) -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    Finally, a data-driven approach to trading psychology. This isn't fluff - it's actionable science.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Independent Trader</strong>
                </div>
            </div>

            <!-- Testimonial 9 (From TPI Page) -->
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p style="font-size: 1.1rem; line-height: 1.6; color: var(--navy); flex-grow: 1;">
                    The assessment pinpointed exactly why I was giving back profits. Game-changing.
                </p>
                <div class="author"
                    style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.05);">
                    <strong style="display: block; color: var(--navy);">Prop Trader</strong>
                </div>
            </div>

        </div>
    </div>
</section>

<!-- Call to Action -->
<section class="section section-dark" style="text-align: center; padding-top: 2rem; padding-bottom: 6rem;">
    <div class="container" style="max-width: 700px;">
        <p class="section-intro" style="margin-bottom: 2rem;">
            Ready to stop self-sabotaging and start scaling?
        </p>
        <a href="<?php echo site_url('/assessment'); ?>" class="btn-primary">Take the Assessment</a>
    </div>
</section>

<?php get_footer(); ?>