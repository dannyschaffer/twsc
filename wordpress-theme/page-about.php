<?php
/**
 * Template Name: About Page
 */

get_header();
?>

<style>
    .hero-about {
        background-color: #ffffff;
        background-image: url('<?php echo get_template_directory_uri(); ?>/assets/images/Topo-Pattern-White.png');
        background-size: cover;
        background-position: center;
        position: relative;
    }

    .hero-about::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('<?php echo get_template_directory_uri(); ?>/assets/images/Topo-Pattern-White.png');
        opacity: 0.4;
        background-size: cover;
        pointer-events: none;
        mix-blend-mode: multiply;
    }

    .bio-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 4rem;
        align-items: center;
        padding: 4rem 0;
    }

    .bio-image img {
        width: 100%;
        border-radius: 4px;
        box-shadow: 20px 20px 0 var(--gold);
    }

    .bio-content h2 {
        font-size: 2.5rem;
        margin-bottom: 2rem;
        color: var(--navy);
    }

    .bio-content p {
        margin-bottom: 1.5rem;
        line-height: 1.8;
        color: var(--text-primary);
    }

    .philosophy-banner {
        background: var(--navy);
        color: #fff;
        padding: 6rem 0;
        text-align: center;
    }

    .philosophy-quote {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-style: italic;
        color: var(--gold);
        max-width: 900px;
        margin: 0 auto 3rem auto;
        line-height: 1.3;
    }

    .philosophy-text {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.2rem;
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.8;
    }

    .credentials-clean {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 4rem;
    }

    .cred-item-clean {
        border-top: 1px solid var(--gold);
        padding-top: 1.5rem;
    }

    .cred-item-clean h3 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: var(--navy);
    }

    .cred-item-clean p {
        color: var(--text-secondary);
        font-size: 0.95rem;
    }

    @media (max-width: 768px) {
        .bio-grid {
            grid-template-columns: 1fr;
        }

        .bio-image {
            order: -1;
        }
    }
</style>

<!-- The Story: Masters of the Universe -->
<section class="section">
    <div class="container">
        <div style="text-align: center; max-width: 900px; margin: 0 auto 4rem auto;">
            <h2 style="font-size: 3rem; margin-bottom: 1rem; color: var(--navy);">I Watched Brilliance Burn
                Out.<br>And Decided to Fix It.</h2>
            <p style="font-size: 1.2rem; color: var(--text-secondary);">My journey from one of the largest hedge
                funds in the world to the
                intersection of neuroscience and elite performance.</p>
        </div>
        <div class="bio-grid">
            <div class="bio-content">
                <p>I spent over a decade in the trenches of finance. I saw the smartest men and women in the
                    room - people with Ivy League degrees and billion-dollar P&Ls - crumble under the weight of
                    their
                    own psychology.</p>
                <p>They were financially rich, but internally bankrupt. They were winning the trade, but losing the
                    war.</p>
                <p><strong>In 2008, the facade cracked.</strong> The financial crisis didn't just break banks; it
                    broke people. I realized that the industry didn't need better algorithms. It needed a new
                    operating system for the human mind.</p>
                <p>I left to study the science of sustainable peak performance. I dove into neuroscience,
                    behavioral finance, and emotional intelligence. I didn't want to just "coach" traders; I wanted
                    to <em>bulletproof</em> them.</p>
            </div>
            <div class="bio-image">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/NY-Kim_Statue.jpg.jpeg"
                    alt="Kim Ann Curtin at NYSE">
            </div>
        </div>
    </div>
</section>

<!-- Philosophy Section -->
<section class="philosophy-banner">
    <div class="container">
        <span
            style="font-family: 'Space Mono', monospace; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7; margin-bottom: 2rem; display: block;">The
            Philosophy</span>
        <blockquote class="philosophy-quote">
            "You already know how to read a chart. I teach you how to read yourself."
        </blockquote>
        <p class="philosophy-text">
            I don't teach technical analysis. My work is for the trader who is tired of self-sabotage. It's for the
            executive who wants to build a legacy, not just a bank account. It's for the few who are ready to do the
            hard, internal work required to become legendary.
        </p>
    </div>
</section>

<!-- Authority / Credentials (No Emojis) -->
<section class="section">
    <div class="container">
        <h2 style="text-align: center; margin-bottom: 2rem;">Authority Built on Results</h2>
        <div class="credentials-clean">
            <div class="cred-item-clean">
                <h3>The Blueprint</h3>
                <p>Author of <em>Transforming Wall Street</em>, the industry-standard text on conscious performance
                    and sustainable success.</p>
            </div>
            <div class="cred-item-clean">
                <h3>The Wall Street 50</h3>
                <p>Learn from the top 50 change-makers and industry titans transforming the financial industry.
                </p>
            </div>
            <div class="cred-item-clean">
                <h3>Battle Tested</h3>
                <p>18+ years coaching inside the world's top hedge funds, sovereign wealth funds, and banks. This
                    isn't
                    theory; it's field experience.</p>
            </div>
            <div class="cred-item-clean">
                <h3>The Network</h3>
                <p>Host of <em>The Wall Street Coach Podcast</em>, featuring in-depth deconstructions of the world's
                    top traders.</p>
            </div>
        </div>
    </div>
</section>

<!-- CTA Section -->
<section class="section" style="background: #f8f9fa; text-align: center;">
    <div class="container" style="max-width: 800px;">
        <h2>Ready to Optimize Your Performance?</h2>
        <p class="section-intro">Your strategy is fine. Your psychology is the bottleneck. Let's fix it.</p>
        <div style="margin-top: 2rem;">
            <a href="<?php echo site_url('/book'); ?>" class="btn-primary" style="margin: 0 1rem;">Book a
                Consultation</a>
        </div>
    </div>
</section>

<?php get_footer(); ?>