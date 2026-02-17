<?php
/**
 * Template Name: Results Page
 */

get_header();

// Testimonial Data Array
$testimonials = [
    [
        'name' => 'Thuan Pham',
        'role' => 'Former CTO of Uber',
        'image' => 'thuan-pham.png',
        'quote' => 'Kim dug deep and delivered her hour-long assessment, my jaw almost hit the table because it felt as if Kim had lived inside my head and fully understood my value system, thought process, and behavioral tendencies. And with that, Kim offered great and pragmatic insights into how I can do even better.'
    ],
    [
        'name' => 'Brian Shannon',
        'role' => 'CMT, Author of Technical Analysis Using Multiple Timeframes',
        'image' => 'brian-shannon.png',
        'quote' => 'Most people will tell you that 90%+ of trading success is mental... Kim helps me explore areas I need to work on and provides actionable insights. If you are committed to success, take the steps to increase your odds, hire Kim!'
    ],
    [
        'name' => 'Howard Lindzon',
        'role' => 'Co-Founder, StockTwits',
        'image' => 'howard-lindzon.jpg',
        'quote' => 'Kim is an excellent executive coach. Her perspective, input and insight over the last few months have helped me hone my brand and focus and plans. Her strategic vision and big picture thinking are second to none.'
    ],
    [
        'name' => 'Tom Burnett',
        'role' => 'Trader',
        'image' => 'tom-burnett.png',
        'quote' => 'In just 6 months of this year, I have been able to grow my account by over 135%. Far exceeding my prior losses, gains, and expectations. Kim and her team are true professionals and the benefits that come from working with them go far beyond earnings and careers.'
    ],
    [
        'name' => 'Andres Armienta',
        'role' => 'Independent Trader',
        'image' => 'andres-armienta.png',
        'quote' => 'My win rate improved from 40% to 60% as I began to trade less and make more... All of the trading work and personal work are very intertwined, and my personal life also got better as I was more observant of how I was interpreting/responding to situations.'
    ],
    [
        'name' => 'Gregg Sciabica',
        'role' => 'Trader',
        'image' => 'gregg-sciabica.png',
        'quote' => 'When one of my traders went into a long drawn out slump I reached out to Kim for help... In just a few weeks she managed to help him get back to consistent profitability. Over the next few months of coaching he transformed into a new person.'
    ],
    [
        'name' => 'Tim Bohen',
        'role' => 'Trader',
        'image' => 'tim-bohen.png',
        'quote' => 'Kim was able to put words to a lot of the common frustrations, issues, and emotions that traders deal with … my colleague and I had some mind-blowing sessions with Kim as well as some major breakthroughs.'
    ],
    [
        'name' => 'Matthew Monaco',
        'role' => 'Trader',
        'image' => 'matthew-monaco.jpg',
        'quote' => 'Working with Kim led to my highest profit month ever, doubling previous records. She\'s helped me improve team processes and uncover hidden obstacles in my mindset. From boosting my confidence to acing job interviews, Kim\'s coaching has been transformative.'
    ],
    [
        'name' => 'Benito Segovia',
        'role' => 'Trader',
        'image' => 'benito-segovia.jpg',
        'quote' => 'Kim is an exceptional coach who has helped numerous TrueTrader members navigate the mental challenges of trading. Her wisdom empowers traders to gain confidence and overcome mental obstacles.'
    ],
    [
        'name' => 'Brian Lee',
        'role' => 'Trader',
        'image' => 'brian-lee.jpg',
        'quote' => 'For me, the work has to do with reconciling my feelings about success, feelings about myself and living my best life while I’m ahead and sustaining it.'
    ],
    [
        'name' => 'Barry Randall',
        'role' => 'CEO, LSC Investment Group',
        'image' => '', // No image
        'quote' => 'I pretty much figured I knew everything... I wasn\'t prepared for the results of the TPI. It gave me real clarity on my biggest hang-ups.'
    ],
    [
        'name' => 'Karim Abdelkader',
        'role' => 'Full Time Trader',
        'image' => '', // No image
        'quote' => 'I have been working with Kim for over a year. And I just had my best January since I began trading 5 years ago... This has everything to do with trading in peace…'
    ],
    [
        'name' => 'Carson Klahm',
        'role' => 'Trader',
        'image' => '', // No image
        'quote' => 'If you are trading as a professional, it is a MUST do. I cannot thank Kim enough.'
    ]
];

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

            <!-- Centered Label -->
            <div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
                <span class="segment-label"
                    style="margin-bottom: 0; color: var(--gold); border-color: var(--gold); display: inline-block; border-bottom: 2px solid; padding-bottom: 2px;">Featured
                    Case Study</span>
            </div>

            <!-- Full Width Image -->
            <div class="results-image-full" style="width: 100%; line-height: 0;">
                <img src="<?php echo get_template_directory_uri(); ?>/assets/images/testimonial 2 2026.png"
                    alt="Significant Trading Performance Metrics" style="width: 100%; height: auto; display: block;">
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

            <?php foreach ($testimonials as $t): ?>
            <div class="testimonial-card-grid"
                style="background: var(--white); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--light-gray); box-shadow: 0 4px 10px rgba(0,0,0,0.03); display: flex; flex-direction: column;">
                <div class="quote-icon"
                    style="color: var(--gold); font-size: 2rem; line-height: 1; margin-bottom: 1rem; font-family: serif;">
                    "</div>
                <p
                    style="font-size: 1.05rem; line-height: 1.6; color: var(--navy); flex-grow: 1; margin-bottom: 1.5rem;">
                    <?php echo $t['quote']; ?>
                </p>

                <div class="author-block"
                    style="margin-top: auto; padding-top: 1.5rem; border-top: 1px solid rgba(0,0,0,0.05); display: flex; align-items: center; gap: 1rem;">
                    <?php if (!empty($t['image'])): ?>
                    <div class="testimonial-headshot" style="flex-shrink: 0;">
                        <img src="<?php echo get_template_directory_uri(); ?>/assets/images/testimonials/<?php echo $t['image']; ?>"
                            alt="<?php echo $t['name']; ?>"
                            style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid var(--gold);">
                    </div>
                    <?php
    endif; ?>

                    <div class="author-info">
                        <strong style="display: block; color: var(--navy); font-size: 1.1rem;">
                            <?php echo $t['name']; ?>
                        </strong>
                        <?php if (!empty($t['role'])): ?>
                        <span
                            style="font-size: 0.85rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px;">
                            <?php echo $t['role']; ?>
                        </span>
                        <?php
    endif; ?>
                    </div>
                </div>
            </div>
            <?php
endforeach; ?>

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