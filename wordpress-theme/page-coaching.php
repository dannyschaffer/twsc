<?php
/**
 * Template Name: Coaching Page
 */

get_header();
?>

    <!-- Split Hero Section -->
    <section class="split-hero">
        <!-- Left: For Traders -->
        <div class="hero-left">
            <span class="segment-label">For Individuals</span>
            <h1 style="color: var(--navy); font-size: 3rem; margin-bottom: 1.5rem;">The Optimized Trader Protocol</h1>
            <p style="color: var(--text-primary); font-size: 1.1rem; margin-bottom: 2rem; max-width: 500px;">
                You don't need another strategy. You need a new nervous system. We combine <strong>neuroscience,
                    biohacking, and elite performance psychology</strong> to break your biological glass ceiling.
            </p>
            <div class="profile-card">
                <h4 style="color: var(--gold); margin-bottom: 1rem;">Ideal For:</h4>
                <ul class="check-list"> <!-- Changed to check-list (dark text) -->
                    <li>Independent Pro Retail Traders</li>
                    <li>Prop Firm Traders hitting a plateau</li>
                    <li>Portfolio Managers</li>
                    <li>High-Performing Executives turning to markets</li>
                </ul>
                <a href="#individual" class="btn-primary" style="margin-top: 1.5rem; display: inline-block;">Explore The
                    Protocol</a>
            </div>
        </div>

        <!-- Right: For Institutions -->
        <div class="hero-right">
            <span class="segment-label">For Institutions</span>
            <h1 style="color: var(--navy); font-size: 3rem; margin-bottom: 1.5rem;">Corporate & Fund Consulting</h1>
            <p style="color: var(--text-primary); font-size: 1.1rem; margin-bottom: 2rem; max-width: 500px;">
                Culture is the ultimate alpha. We help Hedge Funds and Asset Managers build <strong>Anti-Fragile
                    teams</strong> that execute flawlessly under pressure.
            </p>
            <div class="profile-card">
                <h4 style="color: var(--gold); margin-bottom: 1rem;">Ideal For:</h4>
                <ul class="check-list"> <!-- Changed to check-list (dark text) -->
                    <li>Hedge Fund Founders & PMs</li>
                    <li>Trading Desk Heads</li>
                    <li>C-Suite Financial Leaders</li>
                </ul>
                <a href="#corporate" class="btn-secondary"
                    style="margin-top: 1.5rem; display: inline-block; border-color: var(--navy); color: var(--navy);">Explore
                    Consulting</a>
            </div>
        </div>
    </section>

    <!-- Social Proof Banner -->
    <div class="client-logos-strip">
        <div class="container" style="text-align: center;">
            <p
                style="color: var(--navy); opacity: 0.6; font-family: 'Space Mono', monospace; font-size: 0.8rem; margin-bottom: 1.5rem; text-transform: uppercase;">
                Trusted By Professionals At</p>
            <div class="logos-block" style="margin: 0;">
                <div class="hero-logos">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-BlackstoneBW@2x-q633cw8dnd19ck6bb8zwsxltaptwvq6fp2dokvysmc.png"
                        alt="Blackstone">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-BankofAmericaBW@2x-q631b12yl1x2zpgvmtkcd2msrnwizzxsjgt1x3hjla.png"
                        alt="Bank of America">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-CreditSuisseBW@2x-q631coasjm65b52v115u85ou6xsngxgvrlwn5j1qpa.png"
                        alt="Credit Suisse">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-MorganStanleyBW@2x-q630qmz0bg054937pi8prpvstqev0dzfejau3zq0ku.png"
                        alt="Morgan Stanley">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-NBCBW@2x-q631c2oi6fcjw3y9j9tf4t58j2r7jw320mwh45xsoe.png" alt="NBC">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-KingStreetBW@2x-q633tlt35bwrqzwhqh154psthbgtq0inbrwfpz6u0e.png"
                        alt="King Street">
                </div>
                <div class="hero-logos hero-logos-bottom">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-AnchorageBW@2x-q633czzqep6en00upamf2wnno9bdqild1kzmhzt7xg.png"
                        alt="Anchorage">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-FortressBW2@2x-q631g4dhlqvzvo2mwisldadolst3oz5g8o0qi1xrvy.png"
                        alt="Fortress">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-GICBW@2x-q630mp1dngluf4tdqaw1t7p74jufq3byj0sin7kgo4.png" alt="GIC">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-GenentechBW@2x-q633e0nft8kl7sjlr8gva5emuaap2pmw6mfk7sav6s.png"
                        alt="Genentech">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-MerckBW@2x-q633r0r2cqddtlnntut2rva6o67hjz97yzbd7l0t4e.png"
                        alt="Merck">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/Logo-PGBW@2x-q6325e99ddhk27czbg3gewrvms8enzhmdrir1wgokk.png" alt="P&G">
                </div>
            </div>
        </div>
    </div>

    <!-- Testimonials Section -->
    <section class="section section-dark" style="padding-top: 4rem; padding-bottom: 4rem;">
        <div class="container">
            <h2 style="text-align: center; margin-bottom: 2rem; color: var(--navy);">What Traders Are Saying</h2>
            
            <div style="max-width: 800px; margin: 0 auto; text-align: center;">
                <div class="testimonial-carousel">
                    <div class="testimonial-slide active">
                        <blockquote style="font-style: italic; font-size: 1.25rem;">
                            "I pretty much figured I knew everything... I wasn't prepared for the results of the TPI. It
                            gave me real clarity on my biggest hang-ups."
                        </blockquote>
                        <cite><br>Barry Randall, CEO, LSC Investment Group</cite>
                    </div>
                    <div class="testimonial-slide">
                        <blockquote style="font-style: italic; font-size: 1.25rem;">
                            "It felt as if Kim lived inside my head... My jaw almost hit the table."
                        </blockquote>
                        <cite><br><strong>Thuan Q. Pham</strong>, Former CTO of Uber</cite>
                    </div>
                    <div class="testimonial-slide">
                        <blockquote style="font-style: italic; font-size: 1.25rem;">
                            "My win rate improved from 40% to 60% as I began to trade less and make more... The TPI
                            showed me exactly where my issues were stemming from."
                        </blockquote>
                        <cite><br>Andres A., Independent Trader</cite>
                    </div>
                    <div class="testimonial-slide">
                        <blockquote style="font-style: italic; font-size: 1.25rem;">
                            "In just 6 months, I grew my account by over 135%... Far exceeding my prior losses and
                            expectations."
                        </blockquote>
                        <cite><br>Tom Burnett, Trader</cite>
                    </div>
                    <div class="testimonial-slide">
                        <blockquote style="font-style: italic; font-size: 1.25rem;">
                            "If you are trading as a professional, it is a MUST do. I cannot thank Kim enough."
                        </blockquote>
                        <cite><br>Carson Klahm, Trader</cite>
                    </div>
                    <div class="testimonial-slide">
                        <blockquote style="font-style: italic; font-size: 1.25rem;">
                            "I have been working with Kim for over a year. And I just had my best January since I began trading 5 years ago. This has nothing to do with the PnL or win/loss rate or some other metric. And has everything to do with trading in peace…trading with neutrality and unattached to the outcome. Kim helped me find this inner peace. Thank you Kim!"
                        </blockquote>
                        <cite><br>Karim Abdelkader (full time trader)</cite>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- INDIVIDUAL TRACK -->
    <section id="individual" class="section" style="padding-top: 2rem; border-top: none;">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto 4rem auto; text-align: center;">
                <span class="segment-label" style="color: var(--navy); border-color: var(--navy);">01. The Individual
                    Track</span>
                <h2 style="color: var(--navy); font-size: 2.5rem;">Stop Fighting Your Biology</h2>
                <p class="section-intro">Most traders try to fix "mindset" problems with more discipline. But if your
                    cortisol is spiked and your neurotransmitters are depleted, discipline is chemically impossible.</p>
            </div>

            <div class="method-step">
                <div class="method-number">01</div>
                <div class="method-content">
                    <h3>The Biological Audit</h3>
                    <p>We start where others stop: your body. Using an 84-point lab panel, we analyze your hormonal
                        baseline. Are you trading with the testosterone of a predator or the cortisol of prey? We
                        optimize your sleep, recovery, and neurochemistry first.</p>
                </div>
            </div>

            <div class="method-step">
                <div class="method-number">02</div>
                <div class="method-content">
                    <h3>The Trader Positioning Index "Blue Diamond" Analysis</h3>
                    <p>We use the Trader Positioning Index to map your judgment. This isn't a personality test; it's a
                        risk-management diagnostic. We identify exactly where you are leaking alpha - whether it's
                        hesitation (Self-Regard) or impulsivity (Process Adherence).</p>
                </div>
            </div>

            <div class="method-step">
                <div class="method-number">03</div>
                <div class="method-content">
                    <h3>Neural Reprogramming</h3>
                    <p>Once the hardware (body) is optimized, we upgrade the software (mind). Weekly 1:1 strategy
                        sessions focused on "Live Fire" scenarios. We rewrite the subconscious scripts that cause
                        self-sabotage, installing a new operating system for risk.</p>
                </div>
            </div>

            <div class="tech-specs-container"
                style="background: #08333A; color: white; padding: 3rem; border-radius: 12px; margin-top: 4rem;">
                <h3
                    style="color: #fff; margin-bottom: 2rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 1rem;">
                    Protocol Specifications</h3>
                <div class="tech-spec-grid">
                    <div class="spec-item">
                        <h4>Duration</h4>
                        <p>12 Weeks (Intensive)</p>
                    </div>
                    <div class="spec-item">
                        <h4>Access</h4>
                        <p>Weekly 60-min Zoom Strategy Sessions + Direct Text/Voice Access</p>
                    </div>
                    <div class="spec-item">
                        <h4>Diagnostics</h4>
                        <p>Full Trader Positioning Index Profile + Biological Lab Panel Analysis</p>
                    </div>
                    <div class="spec-item">
                        <h4>Outcome</h4>
                        <p>A bespoke "Performance Architecture" document you keep for life.</p>
                    </div>
                </div>
                <!-- CTA Removed -->
            </div>
        </div>
    </section>

    <!-- CORPORATE TRACK -->
    <section id="corporate" class="section section-dark">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto 4rem auto; text-align: center;">
                <span class="segment-label">02. The Institutional Track</span>
                <h2>For Funds That Want to Last</h2>
                <p class="section-intro">Your team's P&L is capped by their psychological capacity. We raise that
                    ceiling.</p>
            </div>

            <div class="corporate-grid">
                <div class="corporate-card">
                    <h3>The "Anti-Fragile" Desk</h3>
                    <p>Most teams crumble under volatility. We build teams that get stronger from it. By aligning the
                        "Collective Judgment" of your desk, we eliminate toxic competition and foster high-performance
                        collaboration.</p>
                </div>
                <div class="corporate-card">
                    <h3>Founder & PM Alignment</h3>
                    <p>When leadership is out of sync, the fund bleeds. We facilitate high-stakes alignment sessions for
                        Partners and PMs to ensure vision, values, and execution are lock-step.</p>
                </div>
                <div class="corporate-card">
                    <h3>Talent Retention & Sourcing</h3>
                    <p>Use the Trader Positioning Index to screen potential hires before they touch your capital.
                        Identify "hidden gem"
                        analysts who have the psychological makeup of top risk-takers.</p>
                </div>
            </div>

            <!-- Removed Corporate Deck Button -->
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto;">
                <h2 style="text-align: center; color: var(--navy);">Start the Conversation</h2>
                <p class="section-intro">Whether you are an individual reaching for new highs or a fund manager building
                    a legacy, it starts here.</p>

                <div style="text-align: center; margin-top: 2rem;">
                    <a href="<?php echo site_url('/book'); ?>" class="btn-primary" style="font-size: 1.2rem; padding: 1rem 3rem;">Schedule a
                        Consultation</a>
                    <p style="margin-top: 1.5rem; opacity: 0.7;">Prefer email? <a
                            href="mailto:info@thewallstreetcoach.com"
                            style="color: var(--navy); text-decoration: underline;">Contact us here</a></p>
                </div>
            </div>
        </div>
    </section>

<?php get_footer(); ?>
