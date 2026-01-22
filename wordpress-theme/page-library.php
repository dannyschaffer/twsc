<?php
/**
 * Template Name: Library Page
 */

get_header();
?>

    <style>
        .library-hero {
            background-color: #F9F9F7;
            color: var(--navy);
            padding: 4rem 0;
            text-align: center;
        }

        .ebook-card {
            background: #fff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            padding: 1.5rem;
            border-radius: 12px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-align: left;
        }

        .ebook-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .ebook-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 1rem;
        }

        .ebooks-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }
    </style>

    <!-- Library Hero -->
    <section class="library-hero">
        <div class="container">
            <h1 style="color: var(--navy); margin-bottom: 1rem;">Your Trading Psychology Library</h1>
            <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                Here are your unlocked resources. Click to download.
            </p>
        </div>
    </section>

    <!-- Main Content -->
    <section class="section">
        <div class="container">
            
            <div class="ebooks-grid">
                <!-- Book 1 -->
                <div class="ebook-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-ego-gremlins.png" alt="EGO and Inner Gremlins">
                    <span style="color: var(--gold); font-family: 'Space Mono', monospace; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px;">Book 1</span>
                    <h3 style="color: var(--navy); margin: 0.5rem 0;">EGO and Inner Gremlins</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-secondary);">Understand and overcome the ego-driven patterns that sabotage your trading decisions.</p>
                    <a href="https://e-bookstwsc.s3.us-east-2.amazonaws.com/Book+1_EGO+and+Inner+Gremlins.pdf" target="_blank" style="color: var(--gold); font-weight: 700; text-decoration: none;">Download PDF →</a>
                </div>

                <!-- Book 2 -->
                <div class="ebook-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-greed-fear.png" alt="Deconstructing Greed and Fear">
                    <span style="color: var(--gold); font-family: 'Space Mono', monospace; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px;">Book 2</span>
                    <h3 style="color: var(--navy); margin: 0.5rem 0;">Deconstructing Greed & Fear</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-secondary);">Learn to recognize and manage the two most powerful emotions in trading.</p>
                    <a href="https://e-bookstwsc.s3.us-east-2.amazonaws.com/Book+2_+Deconstructing+Greed+and+Fear+of+Failure.pdf" target="_blank" style="color: var(--gold); font-weight: 700; text-decoration: none;">Download PDF →</a>
                </div>

                <!-- Book 3 -->
                <div class="ebook-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-fomo-loss.png" alt="Navigating FOMO">
                    <span style="color: var(--gold); font-family: 'Space Mono', monospace; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px;">Book 3</span>
                    <h3 style="color: var(--navy); margin: 0.5rem 0;">Navigating FOMO & Loss</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-secondary);">Master the art of patience and develop a healthy relationship with inevitable losses.</p>
                    <a href="https://e-bookstwsc.s3.us-east-2.amazonaws.com/Book+3_+Navigating+FOMO+and+Comfort+With+Loss.pdf" target="_blank" style="color: var(--gold); font-weight: 700; text-decoration: none;">Download PDF →</a>
                </div>

                <!-- Book 4 -->
                <div class="ebook-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/cover-discipline-edge.png" alt="Discipline and Finding Your Edge">
                    <span style="color: var(--gold); font-family: 'Space Mono', monospace; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px;">Book 4</span>
                    <h3 style="color: var(--navy); margin: 0.5rem 0;">Discipline & Finding Your Edge</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-secondary);">Build unshakeable discipline and discover your unique competitive advantage.</p>
                    <a href="https://e-bookstwsc.s3.us-east-2.amazonaws.com/Book+4_+Discipline+and+Finding+Your+Edge.pdf" target="_blank" style="color: var(--gold); font-weight: 700; text-decoration: none;">Download PDF →</a>
                </div>
            </div>

        </div>
    </section>

<?php get_footer(); ?>
