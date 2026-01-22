<?php
/**
 * Template Name: Podcast Page
 */

get_header();
?>

    <style>
        .podcast-hero {
            background-color: #F9F9F7;
            color: var(--navy);
            padding: 6rem 0;
            text-align: center;
        }

        .featured-legends-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }

        .legend-card {
            background: #fff;
            border: 1px solid rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.3s;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }

        .legend-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
        }

        .legend-image {
            height: 200px;
            background-size: cover;
            background-position: center;
        }

        .legend-content {
            padding: 1.5rem;
            text-align: left;
        }

        .category-tabs {
            display: flex;
            justify-content: center;
            gap: 0.75rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .category-tab {
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #fff;
            padding: 0.5rem 1.25rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 0.9rem;
        }

        .category-tab.active {
            background: var(--gold) !important;
            border-color: var(--gold) !important;
            color: var(--navy) !important;
            font-weight: 600;
        }

        .category-tab:hover:not(.active) {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.5);
        }

        .episodes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .episode-card {
            background: #fff;
            border: 1px solid rgba(0, 0, 0, 0.08);
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
            display: flex;
            flex-direction: column;
        }

        .episode-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .episode-card img {
            width: 100%;
            aspect-ratio: 16 / 9;
            object-fit: contain;
            object-position: center;
            background: #1a1a2e;
        }

        .episode-card-content {
            padding: 1.25rem;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            background: #fff;
        }

        .episode-number {
            color: var(--gold);
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.5rem;
        }

        .episode-title {
            color: var(--navy);
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            line-height: 1.3;
        }

        .episode-description {
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.5;
            margin-bottom: 1rem;
            flex-grow: 1;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .episode-link {
            color: var(--gold);
            font-weight: 700;
            text-decoration: none;
            font-size: 0.9rem;
        }

        .episode-link:hover {
            text-decoration: underline;
        }

        .subscribe-icon {
            display: inline-block;
            transition: transform 0.2s ease;
        }

        .subscribe-icon:hover {
            transform: scale(1.1);
        }

        .browse-section {
            background-color: #F9F9F7;
            padding: 5rem 0;
        }

        .load-more-btn {
            display: block;
            margin: 3rem auto 0;
            padding: 1rem 2.5rem;
            background: var(--navy);
            color: white;
            border: none;
            border-radius: 50px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }

        .load-more-btn:hover {
            background: var(--gold);
            color: var(--navy);
        }

        .episode-count {
            text-align: center;
            color: var(--text-secondary);
            margin-top: 1rem;
            font-size: 0.9rem;
        }
    </style>

    <!-- Podcast Hero -->
    <section class="podcast-hero">
        <div class="container">
            <h1 style="color: var(--navy); margin-bottom: 0.5rem;">The Wall Street Coach Podcast</h1>
            <p style="color: var(--text-secondary); max-width: 700px; margin: 0 auto 3rem auto;">Deconstructing the
                psychology of market wizards. 110+ episodes of insights from legendary traders.</p>

            <div class="subscribe-buttons"
                style="justify-content: center; margin-bottom: 4rem; gap: 1rem; display: flex; flex-wrap: wrap;">
                <!-- Apple Podcasts -->
                <a href="https://podcasts.apple.com/us/podcast/the-wall-street-coach-with-kim-ann-curtin/id1480748536"
                    target="_blank" class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/applepodcasts-icon@2x.png" alt="Apple Podcasts"
                        style="width: 50px; height: 50px;">
                </a>

                <!-- Spotify -->
                <a href="https://open.spotify.com/show/14yIEC46UAHIoO7wsJUAN1" target="_blank" class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/spotify-icon@2x.png" alt="Spotify"
                        style="width: 50px; height: 50px;">
                </a>

                <!-- Google Podcasts -->
                <a href="https://podcasts.google.com/feed/aHR0cHM6Ly93d3cudGhlcGFsbHN0cmVldGNvYWNoLmNvbS9mZWVkLw"
                    target="_blank" class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/googlepodcasts-icon@2x.png" alt="Google Podcasts"
                        style="width: 50px; height: 50px;">
                </a>

                <!-- YouTube -->
                <a href="https://www.youtube.com/channel/UCuApZQaw2UATpJums6cw3HA?view_as=subscriber" target="_blank"
                    class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/youtube-icon@2x.png" alt="YouTube"
                        style="width: 50px; height: 50px;">
                </a>

                <!-- Pandora -->
                <a href="https://www.pandora.com/podcast/the-wall-street-coach/PC:61123?part=PC:61123&corr=podcast_organic_external_site&TID=Brand:POC:PC61123:podcast_organic_external_site"
                    target="_blank" class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/pandora_732234.png" alt="Pandora"
                        style="width: 50px; height: 50px;">
                </a>

                <!-- TuneIn -->
                <a href="https://tunein.com/podcasts/Business--Economics-Podcasts/The-Wall-Street-Coach-Podcast-p1406970/"
                    target="_blank" class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/tunein-icon@2x.png" alt="TuneIn"
                        style="width: 50px; height: 50px;">
                </a>

                <!-- Stitcher -->
                <a href="https://www.stitcher.com/show/the-wall-street-coach" target="_blank" class="subscribe-icon">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/podpage-player-badges/icons/stitcher-icon@2x.png" alt="Stitcher"
                        style="width: 50px; height: 50px;">
                </a>
            </div>

            <!-- Featured Legends -->
            <h3
                style="color: var(--navy); margin-bottom: 2rem; text-align: center; font-family: 'Space Mono', monospace; text-transform: uppercase; font-size: 1rem; letter-spacing: 2px;">
                Featured Legends</h3>
            <div class="featured-legends-grid">
                <!-- Matthew McConaughey -->
                <div class="legend-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/MatthewM.jpg" alt="Matthew McConaughey" class="legend-image"
                        style="width: 100%; height: 280px; object-fit: cover; object-position: center 25%; display: block;">
                    <div class="legend-content">
                        <h4 style="color: var(--navy); margin-bottom: 0.5rem;">Matthew McConaughey</h4>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Greenlights, Resilience, and
                            "Relative Truth"</p>
                        <a href="/episodes/ep-018-episode-18-embracing-greenlights-with-matthew-mcconaughey.html"
                            style="display:inline-block; margin-top:1rem; color: var(--navy); font-size: 0.9rem; font-weight: 600;">Listen
                            Episode →</a>
                    </div>
                </div>
                <!-- Mike Bellafiore -->
                <div class="legend-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/MikeB.jpeg" alt="Mike Bellafiore" class="legend-image"
                        style="width: 100%; height: 280px; object-fit: cover; object-position: center top; display: block;">
                    <div class="legend-content">
                        <h4 style="color: var(--navy); margin-bottom: 0.5rem;">Mike Bellafiore</h4>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Co-Founder of SMB Capital on "One
                            Good Trade"</p>
                        <a href="/episodes/ep-099-ep-99-one-good-trade-with-mike-bellafiore.html"
                            style="display:inline-block; margin-top:1rem; color: var(--navy); font-size: 0.9rem; font-weight: 600;">Listen
                            Episode →</a>
                    </div>
                </div>
                <!-- Jason Shapiro -->
                <div class="legend-card">
                    <img src="<?php echo get_template_directory_uri(); ?>/assets/images/jasonS.png" alt="Jason Shapiro" class="legend-image"
                        style="width: 100%; height: 280px; object-fit: cover; object-position: center center; display: block;">
                    <div class="legend-content">
                        <h4 style="color: var(--navy); margin-bottom: 0.5rem;">Jason Shapiro</h4>
                        <p style="font-size: 0.9rem; color: var(--text-secondary);">Market Wizard on Contrarian Trading
                        </p>
                        <a href="/episodes/ep-076-ep-76-the-contrarian-trading-style-of-unknown-market-wizard-.html"
                            style="display:inline-block; margin-top:1rem; color: var(--navy); font-size: 0.9rem; font-weight: 600;">Listen
                            Episode →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- All Episodes Header Banner -->
    <section class="all-episodes-banner" style="background-color: #08333A; padding: 4rem 0; margin-top: 4rem;">
        <div class="container">
            <h2 style="color: #fff; margin-bottom: 1rem; text-align: center;">All Episodes</h2>
            <p style="text-align: center; color: rgba(255,255,255,0.7); margin-bottom: 2rem;">Browse our complete
                library of 110+ episodes</p>
        </div>
    </section>

    <!-- Episodes Grid Section -->
    <section class="browse-section" style="padding-top: 4rem;">
        <div class="container">
            <div class="episodes-grid" id="episodesGrid">
                <!-- Episodes will be loaded dynamically -->
            </div>

            <p class="episode-count" id="episodeCount"></p>

            <button class="load-more-btn" id="loadMoreBtn" onclick="loadMoreEpisodes()">Load More Episodes</button>

            <div style="margin-top: 3rem; text-align: center;">
                <p style="color: var(--text-secondary); font-size: 0.9rem;">All episodes available right here on the new
                    site!</p>
            </div>
        </div>
    </section>


    <script>
        let currentFilter = 'all';
        let displayedCount = 12;
        const INCREMENT = 12;
        let podcastEpisodes = [];
        // Define directory URI for JS use if needed, but strict path for fetch is best
        const themeDir = '<?php echo get_template_directory_uri(); ?>';

        async function loadEpisodesData() {
            try {
                // Fetch from the JSON in the theme directory
                const response = await fetch('<?php echo get_template_directory_uri(); ?>/podcast-episodes-full.json?nocache=' + new Date().getTime());
                if (!response.ok) throw new Error('Failed to load episodes');
                podcastEpisodes = await response.json();
                renderEpisodes();
            } catch (error) {
                console.error('Error loading podcast episodes:', error);
                document.getElementById('episodesGrid').innerHTML = '<p style="grid-column: 1/-1; text-align: center;">Unable to load episodes. Please try again later.</p>';
            }
        }

        function renderEpisodes() {
            const grid = document.getElementById('episodesGrid');
            if (!podcastEpisodes.length) return;

            // Always use all episodes, sorted by ep number descending if needed (assuming JSON is sorted)
            const filtered = podcastEpisodes;

            const toShow = filtered.slice(0, displayedCount);

            grid.innerHTML = toShow.map(ep => {
                let dateStr = "";
                if (ep.pubDate) {
                    try {
                        const d = new Date(ep.pubDate);
                        dateStr = d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
                    } catch (e) { }
                }

                // Fallback image path handled via JS concatenation to ensure it works
                const fallbackImg = themeDir + '/assets/images/Podcast-Lives.jpeg';

                return `
                <div class="episode-card">
                    <img src="${ep.image}" alt="${ep.title}" onerror="this.src='${fallbackImg}'">
                    <div class="episode-card-content">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.5rem;">
                            <div class="episode-number">Episode ${ep.ep}</div>
                            <div style="color: var(--text-secondary); font-size: 0.8rem;">${dateStr}</div>
                        </div>
                        <h3 class="episode-title">${ep.title}</h3>
                        <p class="episode-description">${ep.description}</p>
                        <a href="${ep.link}" class="episode-link" target="_blank">Listen Episode →</a>
                    </div>
                </div>
                `;
            }).join('');

            // Update count
            document.getElementById('episodeCount').textContent =
                `Showing ${toShow.length} of ${filtered.length} episodes`;

            // Show/hide load more button
            const loadMoreBtn = document.getElementById('loadMoreBtn');
            loadMoreBtn.style.display = displayedCount >= filtered.length ? 'none' : 'block';
        }

        function loadMoreEpisodes() {
            displayedCount += INCREMENT;
            renderEpisodes();
        }

        // Initial render
        loadEpisodesData();
    </script>

<?php get_footer(); ?>
