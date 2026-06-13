<template>
  <div ref="pageRoot" class="site-page">
    <header class="site-header" :class="{ 'site-header--scrolled': isHeaderScrolled, 'site-header--use-cases': isLightHeaderPage }" aria-label="Primary">
      <div class="container site-header__inner">
        <a class="brand" href="/" aria-label="rola-ip home">
          <img class="brand__logo" :src="brandLogo" alt="rola-ip" />
        </a>

        <nav class="site-nav" aria-label="Section navigation">
          <a
            v-for="item in navItems"
            :key="item.label"
            :href="item.href"
            :class="{ 'site-nav__link--active': isNavItemActive(item) }"
          >
            {{ item.label }}
          </a>
        </nav>

        <div class="site-actions">
          <a class="button button--ghost" href="/#faq">Talk to Sales</a>
          <a class="button button--primary" href="/pricing#pricing-page-final">Start Free Trial</a>
        </div>
      </div>
    </header>

    <main v-if="isUseCasesPage" id="top" class="use-cases-page">
      <section class="use-cases-hero">
        <HeroParticles class="hero__particles" :quantity="90" :ease="120" color="#0f9f5a" :staticity="16" />
        <div class="container use-cases-hero__inner">
          <div class="use-cases-hero__copy">
            <span class="section-label section-label--use-cases">Web Scraping</span>
            <h1>Scale Web Scraping &amp; Data Collection Without Getting Blocked.</h1>
            <p>
              Residential and ISP proxies for public data collection teams that need fewer bans,
              cleaner geo coverage, and crawler sessions that survive real production workflows.
            </p>
            <div class="use-cases-hero__actions">
              <a class="button button--primary button--large" href="#scraping-code">Start Free Trial</a>
              <a class="button button--outline button--large" href="/pricing">View Pricing</a>
            </div>
            <div class="use-cases-hero__metrics" aria-label="Web scraping network highlights">
              <div v-for="metric in scrapingHeroStats" :key="metric.label" class="use-cases-hero__metric">
                <strong>{{ metric.value }}</strong>
                <span>{{ metric.label }}</span>
              </div>
            </div>
          </div>

          <aside class="scraping-hero-panel" aria-label="Web scraping collection preview">
            <div class="scraping-hero-panel__top">
              <span class="status-dot"></span>
              <span>Live Collection Run</span>
              <strong>session: sticky-24h</strong>
            </div>
            <div class="scraping-hero-panel__target">
              <span>Target</span>
              <strong>pricing.example.com/products</strong>
              <small>US market · ISP static · retry budget 2</small>
            </div>
            <div class="scraping-hero-panel__flow">
              <span>Proxy route</span>
              <div>
                <i>Collector</i>
                <b></b>
                <i>Rola-IP Gateway</i>
                <b></b>
                <i>Public Web</i>
              </div>
            </div>
            <div class="scraping-hero-panel__jobs">
              <div v-for="job in scrapingHeroJobs" :key="job.label" class="scraping-hero-panel__job">
                <span>{{ job.label }}</span>
                <strong>{{ job.value }}</strong>
              </div>
            </div>
            <div class="scraping-hero-panel__timeline" aria-hidden="true">
              <span v-for="point in scrapingHeroTimeline" :key="point.label" :style="{ '--bar-height': point.height }">
                <i></i>
                <b>{{ point.label }}</b>
              </span>
            </div>
          </aside>
        </div>
      </section>

      <section class="section scraping-challenges">
        <div class="container">
          <div class="section-heading">
            <span class="section-label section-label--why">Scraping Challenges</span>
            <h2>The Problems Scraping Teams Hit Before the Data Arrives.</h2>
            <p>
              Modern targets do not only block volume. They challenge identity, location,
              browser behavior, request timing, and the engineering time needed to keep collectors alive.
            </p>
          </div>

          <div class="scraping-challenge-board">
            <article class="scraping-challenge-summary" aria-label="Scraping risk dashboard">
              <div>
                <span>Target Risk Snapshot</span>
                <strong>Blocked data is usually a routing problem first.</strong>
              </div>
              <div class="scraping-challenge-summary__chart" aria-hidden="true">
                <span v-for="signal in scrapingChallengeSignals" :key="signal.label" :style="{ '--height': signal.height }">
                  <i></i>
                  <b>{{ signal.label }}</b>
                </span>
              </div>
              <div class="scraping-challenge-summary__meta" aria-hidden="true">
                <span v-for="item in scrapingChallengeMeta" :key="item.label">
                  <strong>{{ item.value }}</strong>
                  {{ item.label }}
                </span>
              </div>
            </article>

            <div class="scraping-challenge-grid">
              <article v-for="challenge in scrapingChallenges" :key="challenge.title" class="scraping-challenge-card">
                <component :is="challenge.icon" aria-hidden="true" :size="22" :stroke-width="2" />
                <h3>{{ challenge.title }}</h3>
                <p>{{ challenge.description }}</p>
              </article>
            </div>
          </div>
        </div>
      </section>

      <section class="section scraping-capabilities">
        <div class="container">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--stats">Why Rola-IP</span>
            <h2>Core Proxy Capabilities Behind a More Reliable Data Pipeline.</h2>
            <p>
              Match each target with the right identity behavior: rotate when you need reach,
              stay sticky when continuity matters, and keep routing rules visible to the team.
            </p>
          </div>

          <div class="scraping-feature-mosaic">
            <article class="scraping-feature-card scraping-feature-card--integrations">
              <h3>Pre-Built Scraper Integrations</h3>
              <p>Connect proxy routing to the tools your data team already uses.</p>
              <div class="integration-list" aria-hidden="true">
                <div class="integration-list__header">
                  <span>Ready adapters</span>
                  <div class="integration-connect-pill">
                    <PlugZap aria-hidden="true" :size="17" :stroke-width="2" />
                    Connect
                  </div>
                </div>
                <div v-for="tool in scrapingIntegrationCards" :key="tool.name" class="integration-row" :class="{ 'integration-row--muted': tool.muted }">
                  <span class="integration-row__icon">
                    <component :is="tool.icon" aria-hidden="true" :size="20" :stroke-width="2.2" />
                  </span>
                  <div>
                    <strong>{{ tool.name }}</strong>
                    <small>{{ tool.detail }}</small>
                  </div>
                  <em>Connect</em>
                </div>
              </div>
            </article>

            <article class="scraping-feature-card scraping-feature-card--insights">
              <h3>Cleaner Insights from Every Market</h3>
              <p>Keep geo context, session behavior, and target status visible.</p>
              <div class="insights-stack" aria-hidden="true">
                <div class="insights-panel">
                  <div class="insights-panel__top">
                    <Search aria-hidden="true" :size="20" :stroke-width="2" />
                    <strong>Collection Insights</strong>
                    <em>Live</em>
                  </div>
                  <div class="insights-panel__metric">
                    <span>Clean read rate</span>
                    <b>99.1%</b>
                  </div>
                  <div class="insights-panel__spark">
                    <i v-for="point in scrapingHeroTimeline" :key="`insight-${point.label}`" :style="{ '--bar-height': point.height }"></i>
                  </div>
                  <div class="insights-panel__rows">
                    <span><b></b> US Market</span>
                    <span><b></b> ISP Static</span>
                  </div>
                </div>
              </div>
            </article>

            <article class="scraping-feature-card scraping-feature-card--support">
              <h3>Routing Diagnostics Before Rollout</h3>
              <p>Review target risk, country coverage, and sticky-session strategy.</p>
              <div class="routing-diagnostics" aria-hidden="true">
                <div class="routing-diagnostics__score">
                  <span>Route health</span>
                  <strong>96%</strong>
                </div>
                <div class="routing-diagnostics__rows">
                  <div v-for="row in routingDiagnostics" :key="row.label">
                    <span>{{ row.label }}</span>
                    <b>{{ row.value }}</b>
                    <i :style="{ '--fill': row.fill }"></i>
                  </div>
                </div>
              </div>
            </article>

            <article class="scraping-feature-card scraping-feature-card--metric">
              <div class="metric-visual metric-visual--ledger" aria-hidden="true">
                <div>
                  <span>
                    <Zap aria-hidden="true" :size="22" :stroke-width="2.4" />
                  </span>
                  <strong>42.8K</strong>
                </div>
                <i v-for="job in scrapingHeroJobs" :key="`metric-${job.label}`">
                  <b>{{ job.label }}</b>
                  <em>{{ job.value }}</em>
                </i>
              </div>
              <h3>Stable High-Volume Collection</h3>
              <p>Scale request volume without losing track of clean reads and retries.</p>
            </article>

            <article class="scraping-feature-card scraping-feature-card--code">
              <div class="developer-setup-visual" aria-hidden="true">
                <div class="developer-setup-visual__glow"></div>
                <div class="setup-tool-strip">
                  <span>
                    <TerminalSquare aria-hidden="true" :size="15" :stroke-width="2" />
                    curl
                  </span>
                  <span>
                    <Code2 aria-hidden="true" :size="15" :stroke-width="2" />
                    Python
                  </span>
                  <span>
                    <ScanSearch aria-hidden="true" :size="15" :stroke-width="2" />
                    Playwright
                  </span>
                </div>
                <div class="setup-flow">
                  <div class="setup-code-panel">
                    <div class="setup-code-panel__bar">
                      <span>proxy.config</span>
                      <i></i>
                      <i></i>
                      <i></i>
                    </div>
                    <pre>session = "sticky-24h"
route.country = "US"
proxy.type = "ISP"</pre>
                  </div>
                  <div class="setup-connector">
                    <i>
                      <PlugZap aria-hidden="true" :size="18" :stroke-width="2.2" />
                    </i>
                  </div>
                  <div class="setup-endpoint-card">
                    <span class="setup-endpoint-card__icon">
                      <ShieldCheck aria-hidden="true" :size="20" :stroke-width="2.2" />
                    </span>
                    <strong>Auth OK</strong>
                    <small>proxy.rola.com:9000</small>
                    <em>
                      <KeyRound aria-hidden="true" :size="13" :stroke-width="2.1" />
                      Sticky 24h
                    </em>
                    <em>
                      <Globe2 aria-hidden="true" :size="13" :stroke-width="2.1" />
                      US route
                    </em>
                  </div>
                </div>
                <div class="setup-quick-row">
                  <span>
                    <Route aria-hidden="true" :size="14" :stroke-width="2" />
                    Rotating or sticky
                  </span>
                  <span>
                    <Code2 aria-hidden="true" :size="14" :stroke-width="2" />
                    3-line config
                  </span>
                </div>
              </div>
              <div class="scraping-feature-card__copy">
                <h3>Developer-Friendly Setup</h3>
                <p>Use standard proxy auth with curl, Python, Node, Playwright, or Scrapy.</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section id="proxy-fit" class="section section--alt proxy-fit-section">
        <div class="container proxy-fit-layout">
          <div class="section-heading">
            <span class="section-label section-label--definition">Proxy Fit</span>
            <h2>Choose the Proxy Type by Target Risk, Speed, and Session Needs.</h2>
            <p>
              Use this as the buyer education layer: not every scraping job needs the same proxy
              behavior, cost model, or trust signal.
            </p>
          </div>

          <div class="proxy-type-grid" aria-label="Proxy type fit for scraping">
            <article v-for="row in scrapingProxyFit" :key="row.type" class="proxy-type-card">
              <span class="proxy-type-card__icon">
                <component :is="row.icon" aria-hidden="true" :size="20" :stroke-width="2" />
              </span>
              <span class="proxy-type-card__price">{{ row.price }}</span>
              <h3>{{ row.type }}</h3>
              <p>{{ row.fit }}</p>
              <small>{{ row.note }}</small>
            </article>
          </div>
        </div>
      </section>

      <section id="scraping-code" class="section section--dark quick-start-section scraping-code-section">
        <div class="container quick-start scraping-code-layout">
          <div class="quick-start__copy scraping-code-copy">
            <span class="section-label section-label--dark section-label--quick">Quick Start</span>
            <h2>Ship Your First <span class="grad-text grad-text--dark">Scraping Request</span> in Minutes.</h2>
            <div class="quick-start__list">
              <article v-for="item in quickStartItems" :key="item.title" class="quick-start-card">
                <span class="icon-tile icon-tile--dark">
                  <component :is="item.icon" aria-hidden="true" :size="18" :stroke-width="2" />
                </span>
                <h3>{{ item.title }}</h3>
              </article>
            </div>
          </div>

          <div class="quick-start__code">
            <div class="code-editor" aria-label="Web scraping proxy integration example">
              <div class="code-editor__header">
                <div class="code-editor__tabs" aria-label="Code language tabs">
                  <button
                    v-for="tab in codeTabs"
                    :key="tab.key"
                    class="code-editor__tab"
                    :class="{ 'code-editor__tab--active': activeCodeTab === tab.key }"
                    type="button"
                    :aria-pressed="activeCodeTab === tab.key"
                    @click="activeCodeTab = tab.key"
                  >
                    <img class="code-editor__logo" :src="tab.logo" alt="" aria-hidden="true" />
                    {{ tab.label }}
                  </button>
                </div>
                <div class="code-editor__actions">
                  <span class="code-editor__icon" aria-label="Request example info" title="Request example info">
                    <TerminalSquare aria-hidden="true" :size="18" :stroke-width="1.9" />
                  </span>
                  <button class="code-editor__copy" type="button" :aria-label="hasCopiedCode ? 'Copied' : 'Copy code'" @click="copyCodeSample">
                    <component :is="hasCopiedCode ? CheckCircle2 : Copy" aria-hidden="true" :size="18" :stroke-width="1.9" />
                  </button>
                </div>
              </div>
              <pre><code><span v-for="line in codeSampleLines" :key="line.number" class="code-editor__line"><span class="code-editor__line-number">{{ line.number }}</span><span class="code-editor__line-text"><span v-for="(token, tokenIndex) in line.tokens" :key="`${line.number}-${tokenIndex}`" :class="`code-token code-token--${token.kind}`">{{ token.value }}</span></span></span></code></pre>
            </div>
          </div>
        </div>
      </section>

      <section class="section use-cases-directory">
        <div class="container">
          <div class="section-heading">
            <span class="section-label section-label--use-cases">Use Cases</span>
            <h2>High-Value Data Collection Scenarios Worth Designing Around.</h2>
            <p>
              Help each buyer recognize their workflow quickly, then route them toward the proxy
              behavior that best fits that target.
            </p>
          </div>

          <div class="use-cases-page-grid">
            <article
              v-for="(useCase, index) in displayedScrapingUseCases"
              :key="useCase.title"
              class="use-cases-page-card"
              :class="{ 'use-cases-page-card--featured': index === 0 }"
            >
              <span class="use-cases-page-card__index">0{{ index + 1 }}</span>
              <span class="icon-tile use-cases-page-card__icon">
                <component :is="useCase.icon" aria-hidden="true" :size="20" :stroke-width="2" />
              </span>
              <h3>{{ useCase.title }}</h3>
              <p>{{ useCase.description }}</p>
              <div v-if="index === 0" class="use-cases-page-card__preview" aria-hidden="true">
                <span v-for="point in scrapingHeroTimeline.slice(0, 5)" :key="`case-${point.label}`" :style="{ '--bar-height': point.height }"></span>
              </div>
              <span class="use-cases-page-card__signal">{{ useCase.signal }}</span>
            </article>
          </div>
        </div>
      </section>

      <section class="section scraping-compliance-section">
        <div class="container scraping-compliance-panel">
          <div>
            <span class="section-label section-label--compliance">Compliance</span>
            <h2>Scrape Public Data with Clear Usage Boundaries.</h2>
          </div>
          <p>
            Rola-IP is designed for legitimate research, monitoring, and automation. Enterprise
            teams can request sourcing details, privacy terms, and security documentation before
            rollout.
          </p>
        </div>
      </section>

      <section class="section scraping-proof-section">
        <div class="container scraping-proof-layout">
          <div class="section-heading">
            <span class="section-label section-label--testimonials">Proof</span>
            <h2>Trusted by Teams That Treat Data Collection as Infrastructure.</h2>
            <p>
              Social proof should make the page feel procurement-ready: practical quotes,
              review-platform badges, and clear signals that real operators use the network.
            </p>
            <div class="scraping-awards" aria-label="Review and media signals">
              <span v-for="award in scrapingAwards" :key="award">{{ award }}</span>
            </div>
          </div>

          <div class="scraping-proof-window">
            <div class="scraping-proof-grid">
              <article
                v-for="quote in visibleScrapingTestimonials"
                :key="quote.slot"
                class="scraping-proof-card"
              >
                <div class="scraping-proof-card__rating" aria-label="5 star rating">★★★★★</div>
                <p>{{ quote.quote }}</p>
                <div class="scraping-proof-card__author">
                  <img :src="quote.avatar" alt="" aria-hidden="true" />
                  <div>
                    <strong>{{ quote.author }}</strong>
                    <span>{{ quote.role }}</span>
                  </div>
                </div>
              </article>
            </div>
            <span class="scraping-proof-window__fade" aria-hidden="true"></span>
          </div>
        </div>
      </section>

      <section id="use-case-faq" class="section faq-section use-cases-faq">
        <div class="container faq-wrap">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--faq">FAQ</span>
            <h2>Questions Scraping Teams Ask Before Rollout.</h2>
          </div>

          <div class="faq-list">
            <details
              v-for="(item, index) in scrapingFaqItems"
              :key="item.question"
              class="faq-item"
              :open="openUseCaseFaqIndex === index"
            >
              <summary @click.prevent="openUseCaseFaq(index)">
                <span>{{ item.question }}</span>
              </summary>
              <p>{{ item.answer }}</p>
            </details>
          </div>
        </div>
      </section>

      <section class="final-cta">
        <div class="container final-cta__inner">
          <span class="section-label section-label--dark section-label--ready">Ready to Scrape</span>
          <h2>Map the Target, Pick the Proxy Type, Then Launch with Stable Sessions.</h2>
          <p>
            Start with a small ISP proxy setup for a high-value scraping workflow, then expand
            coverage and routing rules once your collection logic is validated.
          </p>
          <div class="final-cta__actions">
            <a class="button button--primary button--large" href="/pricing#pricing-page-final">Start Free Trial</a>
            <a class="button button--dark-outline button--large" href="/#faq">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isPricingPage" id="top" class="pricing-page">
      <section class="pricing-page__intro">
        <div class="container pricing-page__intro-inner">
          <div class="pricing-page__heading">
            <span class="section-label section-label--pricing">Pricing</span>
            <h1>Simple Static ISP Proxy Pricing</h1>
            <p>
              Pick a per-IP package, validate routing with a smaller allocation, then scale into
              larger inventory when the workflow is proven.
            </p>
          </div>

          <div class="pricing-page__metrics" aria-label="Pricing proof points">
            <article v-for="metric in pricingPageMetrics" :key="metric.label">
              <component :is="metric.icon" aria-hidden="true" :size="18" :stroke-width="2.2" />
              <strong>{{ metric.value }}</strong>
              <span>{{ metric.label }}</span>
            </article>
          </div>

          <div class="pricing-table-shell">
            <div class="pricing-table-top">
              <div>
                <span class="pricing-model-pill">Static ISP / per-IP</span>
                <p>Monthly packages for predictable inventory planning, with custom sourcing for larger deployments.</p>
              </div>
              <div class="pricing-mode-toggle" aria-label="Pricing model options">
                <span class="pricing-mode-toggle__item pricing-mode-toggle__item--active">Monthly plans</span>
                <span class="pricing-mode-toggle__item">Custom terms</span>
              </div>
            </div>

            <div class="pricing-page-plan-grid">
              <article
                v-for="plan in pricingPagePlans"
                :key="plan.name"
                class="pricing-page-card"
                :class="{ 'pricing-page-card--featured': plan.featured }"
              >
                <p v-if="plan.featured" class="pricing-page-card__badge">Most Popular</p>
                <div class="pricing-page-card__top">
                  <span class="icon-tile pricing-page-card__icon">
                    <component :is="plan.icon" aria-hidden="true" :size="19" :stroke-width="2" />
                  </span>
                  <div>
                    <p class="pricing-page-card__name">{{ plan.name }}</p>
                    <p class="pricing-page-card__fit">{{ plan.fit }}</p>
                  </div>
                </div>
                <p class="pricing-page-card__volume">{{ plan.ipCount }}</p>
                <p class="pricing-page-card__price">{{ plan.price }}</p>
                <p class="pricing-page-card__monthly">{{ plan.monthly }}</p>
                <ul class="pricing-page-card__list">
                  <li v-for="item in plan.items" :key="item">
                    <CheckCircle2 aria-hidden="true" :size="15" :stroke-width="2.4" />
                    <span>{{ item }}</span>
                  </li>
                </ul>
                <a class="button" :class="plan.featured ? 'button--primary' : 'button--outline'" href="#pricing-page-final">
                  {{ plan.cta }}
                </a>
              </article>
            </div>

            <div class="pricing-table-notes" aria-label="Billing notes">
              <span v-for="note in pricingPageNotes" :key="note">{{ note }}</span>
            </div>
          </div>
        </div>
      </section>

      <section class="section pricing-page-includes">
        <div class="container pricing-page-split">
          <div class="pricing-page-copy">
            <span class="section-label section-label--definition">Every Plan Includes</span>
            <h2>Lower Tiers Keep the Same Core Controls.</h2>
            <p>
              Make the first purchase feel safe: the table changes inventory size and support
              depth, not the basic proxy controls teams need to validate a workflow.
            </p>
          </div>
          <div class="pricing-page-include-grid">
            <article v-for="item in pricingPlanIncludes" :key="item.title" class="pricing-page-include-card">
              <CheckCircle2 aria-hidden="true" :size="17" :stroke-width="2.4" />
              <div>
                <h3>{{ item.title }}</h3>
                <p>{{ item.description }}</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section class="section section--alt pricing-page-billing">
        <div class="container pricing-page-split">
          <div class="pricing-page-copy">
            <span class="section-label section-label--why">Billing Fit</span>
            <h2>Transparent Cost Math Before Procurement Starts.</h2>
            <p>
              Competitor pricing often forces buyers through bandwidth calculators, minimum
              commitments, and unclear rules. This page keeps ISP pricing tied to inventory size.
            </p>
          </div>
          <div class="pricing-page-billing-grid">
            <article v-for="item in pricingBillingCards" :key="item.title" class="pricing-page-billing-card">
              <component :is="item.icon" aria-hidden="true" :size="21" :stroke-width="2" />
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section pricing-page-capabilities">
        <div class="container">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--stats">Why It Is Worth the Price</span>
            <h2>Capabilities That Make Static ISP Inventory Easier to Justify.</h2>
          </div>
          <div class="pricing-page-capability-grid">
            <article v-for="item in pricingCapabilities" :key="item.title" class="pricing-page-capability-card">
              <span class="icon-tile pricing-page-capability-card__icon">
                <component :is="item.icon" aria-hidden="true" :size="20" :stroke-width="2" />
              </span>
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section section--alt pricing-page-trust">
        <div class="container">
          <div class="pricing-trust-panel">
            <div class="pricing-page-copy">
              <span class="section-label section-label--testimonials">Trust Signals</span>
              <h2>Proof for Buyers Comparing More Than Unit Price.</h2>
              <p>
                Procurement teams need review signals, operator quotes, and a clear support story
                before they move from a test allocation to production.
              </p>
            </div>
            <div class="pricing-review-strip" aria-label="Review sources">
              <article v-for="review in pricingReviewSignals" :key="review.label">
                <img :src="review.logo" :alt="review.alt" />
                <strong>{{ review.value }}</strong>
                <span>{{ review.label }}</span>
              </article>
            </div>
            <div class="pricing-testimonial-grid">
              <article v-for="quote in pricingTestimonials" :key="quote.author" class="pricing-testimonial-card">
                <div aria-label="Five-star review">★★★★★</div>
                <p>"{{ quote.quote }}"</p>
                <span>{{ quote.author }}</span>
              </article>
            </div>
          </div>
        </div>
      </section>

      <section class="section pricing-page-security">
        <div class="container pricing-security-panel">
          <div class="pricing-page-copy">
            <span class="section-label section-label--compliance">Secure Purchase</span>
            <h2>Payment, Sourcing, and Review Details Stay Clear.</h2>
            <p>
              Keep the buying moment calm with explicit security signals, acceptable-use review,
              and procurement support for enterprise plans.
            </p>
          </div>
          <div class="pricing-security-grid">
            <article v-for="item in pricingSecurityItems" :key="item.title">
              <component :is="item.icon" aria-hidden="true" :size="20" :stroke-width="2" />
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
            </article>
          </div>
        </div>
      </section>

      <section id="pricing-page-faq" class="section faq-section pricing-page-faq">
        <div class="container faq-wrap">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--faq">Billing FAQ</span>
            <h2>Questions Buyers Ask Before Checkout.</h2>
          </div>

          <div class="faq-list">
            <details
              v-for="(item, index) in pricingPageFaqItems"
              :key="item.question"
              class="faq-item"
              :open="openPricingPageFaqIndex === index"
            >
              <summary @click.prevent="openPricingPageFaq(index)">
                <span>{{ item.question }}</span>
              </summary>
              <p>{{ item.answer }}</p>
            </details>
          </div>
        </div>
      </section>

      <section id="pricing-page-final" class="final-cta pricing-page-final">
        <div class="container final-cta__inner">
          <span class="section-label section-label--dark section-label--ready">Ready to Start</span>
          <h2>Validate a Small Allocation, Then Scale the Same Pricing Model.</h2>
          <p>
            Start with static ISP inventory for one serious workflow, or talk to sales for custom
            markets, security review, and enterprise terms.
          </p>
          <div class="final-cta__actions">
            <a class="button button--primary button--large" href="/#quick-start">Start Free Trial</a>
            <a class="button button--dark-outline button--large" href="#pricing-page-faq">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <main v-else id="top">
      <section class="hero">
        <HeroParticles class="hero__particles" :quantity="150" :ease="120" color="#70f3a8" :staticity="10" />
        <div class="container hero__grid">
          <div class="hero__content">
            <h1>
              <span class="grad-text">ISP / Static</span>
              <br />
              <span class="grad-text">Residential Proxies</span>
            </h1>
            <p class="hero__sub">
              Stable ISP-assigned identities for teams running account operations, verification,
              research, and automation, with predictable per-IP pricing instead of messy bandwidth
              math.
            </p>

            <div class="hero__actions">
              <a class="button button--primary button--large" href="#pricing">Start Free Trial</a>
              <a class="button button--outline button--large" href="#quick-start">See Quick Start</a>
            </div>

            <div class="hero__meta">
              <span v-for="item in heroMeta" :key="item" class="hero__meta-item">{{ item }}</span>
            </div>
          </div>

          <aside class="hero-demo" aria-label="Proxy demo card">
            <div class="hero-demo__header">
              <div class="hero-demo__status">
                <span class="status-dot"></span>
                <span>Live Sticky Session</span>
              </div>
              <span class="hero-demo__tag">Session ID: RO-2419</span>
            </div>

            <p class="hero-demo__ip">185.232.21.84</p>

            <div class="hero-demo__fields">
              <div v-for="field in heroCardFields" :key="field.label" class="hero-demo__field">
                <p class="hero-demo__label">{{ field.label }}</p>
                <p class="hero-demo__value" :class="{ 'is-placeholder': isPlaceholder(field.value) }">
                  {{ field.value }}
                </p>
              </div>
            </div>

            <div class="hero-demo__footer">
              <div class="signal-bars" aria-hidden="true">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
              </div>
              <span class="hero-demo__latency">latency: 0.58s avg</span>
            </div>

            <div class="hero-demo__code">
              <span class="hero-demo__code-accent">curl</span>
              <span>-x gateway.rola-ip.com --session sticky-session-01</span>
            </div>
          </aside>
        </div>
      </section>

      <section class="proof-section" aria-label="Trust and performance proof">
        <div class="container proof-panel">
          <div class="trust-bar__inner">
            <div v-for="item in trustItems" :key="item.label" class="trust-item" :class="{ 'trust-item--teams': !item.logo }">
              <span class="trust-item__mark" aria-hidden="true">
                <img v-if="item.logo" :src="item.logo" :alt="item.alt" />
                <BadgeCheck v-else :size="20" :stroke-width="2.3" />
              </span>
              <span class="trust-item__body">
                <span class="trust-item__source">{{ item.source }}</span>
                <span class="trust-item__value" :class="{ 'is-placeholder': isPlaceholder(item.value) }">
                  {{ item.value }}
                </span>
                <span class="trust-item__label">{{ item.label }}</span>
              </span>
            </div>
          </div>

          <div class="stats-row">
            <article v-for="stat in stats" :key="stat.label" class="stat-card">
              <component :is="stat.icon" class="stat-card__icon" aria-hidden="true" :size="20" :stroke-width="2" />
              <p class="stat-card__value" :class="{ 'is-placeholder': isPlaceholder(stat.value) }">
                {{ stat.value }}
              </p>
              <p class="stat-card__label">{{ stat.label }}</p>
            </article>
          </div>
        </div>
      </section>

      <section id="features" class="section performance-section">
        <div class="container performance-layout">
          <div class="performance-copy">
            <span class="section-label section-label--stats">Performance Stats</span>
            <h2>Proven by Teams Running High-Trust Proxy Workflows.</h2>
            <p>
              Improve session continuity, reduce avoidable retries, and make proxy costs easier
              to forecast before production rollout.
            </p>
            <a class="performance-copy__link" href="#quick-start">
              Explore the Quick Start
              <span aria-hidden="true">-&gt;</span>
            </a>
            <div class="feature-steps__social">
              <span class="feature-steps__avatars" aria-hidden="true">
                <img v-for="avatar in socialAvatars" :key="avatar" :src="avatar" alt="" />
              </span>
              <span>20,000+ research and automation users compare routing, pricing, and proof before launch.</span>
            </div>
          </div>

          <div class="performance-card-grid" aria-label="Performance highlights">
            <article
              v-for="(card, index) in performanceCards"
              :key="card.label"
              class="performance-card"
              :class="{ 'performance-card--large': index === 0 }"
            >
              <p class="performance-card__label">
                <component :is="card.icon" aria-hidden="true" :size="19" :stroke-width="2.3" />
                <span>{{ card.label }}</span>
              </p>
              <p class="performance-card__value">{{ card.value }}</p>
              <p class="performance-card__desc">{{ card.description }}</p>
            </article>
          </div>
        </div>
      </section>

      <section id="pricing" class="section section--alt">
        <div class="container">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--pricing">Pricing</span>
            <h2>Transparent <span class="grad-text">per-IP Plans</span> for Teams That Need Predictable Scaling.</h2>
            <p>
              Start with 10 static ISP IPs, scale into 500+ IP packages, or request dedicated
              inventory with custom routing and procurement support.
            </p>
          </div>

          <div class="pricing-grid">
            <article
              v-for="plan in pricingPlans"
              :key="plan.name"
              class="pricing-card"
              :class="{ 'pricing-card--featured': plan.featured }"
            >
              <p v-if="plan.featured" class="pricing-card__badge">Most Popular</p>
              <div class="pricing-card__top">
                <span class="icon-tile pricing-card__icon">
                  <component :is="plan.icon" aria-hidden="true" :size="19" :stroke-width="2" />
                </span>
                <p class="pricing-card__name">{{ plan.name }}</p>
              </div>
              <p class="pricing-card__volume" :class="{ 'is-placeholder': isPlaceholder(plan.ipCount) }">
                {{ plan.ipCount }}
              </p>
              <p class="pricing-card__price" :class="{ 'is-placeholder': isPlaceholder(plan.price) }">
                {{ plan.price }}
              </p>
              <ul class="pricing-card__list">
                <li v-for="item in plan.items" :key="item">
                  <CheckCircle2 aria-hidden="true" :size="15" :stroke-width="2.4" />
                  <span>{{ item }}</span>
                </li>
              </ul>
              <a class="button" :class="plan.featured ? 'button--primary' : 'button--outline'" href="#faq">
                {{ plan.cta }}
              </a>
            </article>
          </div>
        </div>
      </section>

      <section id="coverage" class="section">
        <div class="container">
          <div class="section-heading">
            <span class="section-label section-label--coverage">Geo Coverage</span>
            <h2>Coverage Across <span class="grad-text">Priority Markets</span> Where Buyers Usually Ask First.</h2>
            <p>
              Show the footprint at a glance, then let visitors scan the key regions they need for
              research, verification, monitoring, and account operations.
            </p>
          </div>

          <div class="coverage-overview">
            <div>
              <p class="coverage-overview__label">Launch Coverage Snapshot</p>
              <p class="coverage-overview__value" :class="{ 'is-placeholder': isPlaceholder(coverageSummary) }">
                {{ coverageSummary }}
              </p>
            </div>
            <p class="coverage-overview__text">
              Access ISP-backed coverage across major commercial markets, with country targeting,
              sticky sessions, and routing rules available from the dashboard.
            </p>
          </div>

          <div class="coverage-grid">
            <article v-for="region in coverage" :key="region.name" class="coverage-card">
              <span class="coverage-card__flag">{{ region.flag }}</span>
              <p class="coverage-card__name">{{ region.name }}</p>
              <p class="coverage-card__count" :class="{ 'is-placeholder': isPlaceholder(region.count) }">
                {{ region.count }}
              </p>
            </article>
          </div>
        </div>
      </section>

      <section class="section section--dark network-section" aria-labelledby="network-title">
        <div class="container network-grid">
          <div class="network-copy">
            <span class="section-label section-label--dark section-label--network">Network Operations</span>
            <h2 id="network-title"><span class="grad-text grad-text--dark">Control Sessions</span>, Routing, and Rollout Rules from One Operational Layer.</h2>
            <p>
              Monitor 1.3M+ static ISP identities through one control layer, with country rules,
              session persistence, and traffic visibility designed for production teams.
            </p>
          </div>

          <div class="network-panel" aria-label="Network operation highlights">
            <article v-for="item in networkSignals" :key="item.title" class="network-card">
              <span class="icon-tile icon-tile--dark">
                <component :is="item.icon" aria-hidden="true" :size="20" :stroke-width="2" />
              </span>
              <p class="network-card__kicker">{{ item.kicker }}</p>
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
            </article>
          </div>
        </div>
      </section>

      <section id="use-cases" class="section section--alt">
        <div class="container">
          <div class="section-heading">
            <span class="section-label section-label--use-cases">Use Cases</span>
            <h2>Built for Teams That Need Session Stability, Not Just Raw Request Volume.</h2>
          </div>

          <div class="use-case-grid">
            <article v-for="(useCase, index) in useCases" :key="useCase.title" class="use-case-card">
              <div class="use-case-card__top">
                <span class="icon-tile use-case-card__icon">
                  <component :is="useCase.icon" aria-hidden="true" :size="20" :stroke-width="2" />
                </span>
                <span class="use-case-card__number">0{{ index + 1 }}</span>
              </div>
              <h3>{{ useCase.title }}</h3>
              <p>{{ useCase.description }}</p>
              <span class="use-case-card__signal">{{ useCase.signal }}</span>
            </article>
          </div>
        </div>
      </section>

      <section id="quick-start" class="section section--dark quick-start-section">
        <div class="container quick-start">
          <div class="quick-start__copy">
            <span class="section-label section-label--dark section-label--quick">Quick Start</span>
            <h2>Ship Your First <span class="grad-text grad-text--dark">Sticky-Session Request</span> in Minutes.</h2>
            <div class="quick-start__list">
              <article v-for="item in quickStartItems" :key="item.title" class="quick-start-card">
                <span class="icon-tile icon-tile--dark">
                  <component :is="item.icon" aria-hidden="true" :size="18" :stroke-width="2" />
                </span>
                <h3>{{ item.title }}</h3>
              </article>
            </div>
          </div>

          <div class="quick-start__code">
            <div class="code-editor" aria-label="Curl quick start example">
              <div class="code-editor__header">
                <div class="code-editor__tabs" aria-label="Code language tabs">
                  <button
                    v-for="tab in codeTabs"
                    :key="tab.key"
                    class="code-editor__tab"
                    :class="{ 'code-editor__tab--active': activeCodeTab === tab.key }"
                    type="button"
                    :aria-pressed="activeCodeTab === tab.key"
                    @click="activeCodeTab = tab.key"
                  >
                    <img class="code-editor__logo" :src="tab.logo" alt="" aria-hidden="true" />
                    {{ tab.label }}
                  </button>
                </div>
                <div class="code-editor__actions">
                  <span class="code-editor__icon" aria-label="Request example info" title="Request example info">
                    <TerminalSquare aria-hidden="true" :size="18" :stroke-width="1.9" />
                  </span>
                  <button class="code-editor__copy" type="button" :aria-label="hasCopiedCode ? 'Copied' : 'Copy code'" @click="copyCodeSample">
                    <component :is="hasCopiedCode ? CheckCircle2 : Copy" aria-hidden="true" :size="18" :stroke-width="1.9" />
                  </button>
                </div>
              </div>
              <pre><code><span v-for="line in codeSampleLines" :key="line.number" class="code-editor__line"><span class="code-editor__line-number">{{ line.number }}</span><span class="code-editor__line-text"><span v-for="(token, tokenIndex) in line.tokens" :key="`${line.number}-${tokenIndex}`" :class="`code-token code-token--${token.kind}`">{{ token.value }}</span></span></span></code></pre>
            </div>
          </div>
        </div>
      </section>

      <section class="section section--alt">
        <div class="container compare-grid">
          <div>
            <div class="section-heading">
              <span class="section-label section-label--why">Why ISP</span>
              <h2>Why Static ISP Proxies Outperform on Session-Sensitive Workflows.</h2>
              <p>
                Help buyers understand when to choose static ISP proxies over rotating residential
                or datacenter options, especially for login-heavy and stateful use cases.
              </p>
            </div>

            <div class="compare-table" role="table" aria-label="Proxy comparison">
              <div class="compare-table__head" role="row">
                <span>Comparison Point</span>
                <span>ISP Static</span>
                <span>Rotating Residential</span>
                <span>Datacenter</span>
              </div>

              <div v-for="row in comparisonRows" :key="row.label" class="compare-table__row" role="row">
                <span class="compare-table__cell compare-table__cell--label" data-label="Comparison point">
                  {{ row.label }}
                </span>
                <span class="compare-table__cell compare-table__cell--accent" data-label="ISP static">
                  {{ row.isp }}
                </span>
                <span class="compare-table__cell" data-label="Rotating residential">{{ row.rotating }}</span>
                <span class="compare-table__cell" data-label="Datacenter">{{ row.datacenter }}</span>
              </div>
            </div>
          </div>

          <aside class="explain-card">
            <span class="section-label section-label--definition">Definition</span>
            <h3>Static Residential Proxies Combine Residential Trust Signals with Datacenter-Grade Stability.</h3>
            <p>
              That makes them especially useful for login-heavy, session-sensitive, or longer-lived
              workflows where rotating identities can break continuity.
            </p>
            <ul class="explain-card__list">
              <li v-for="item in explainBullets" :key="item">
                <CheckCircle2 aria-hidden="true" :size="15" :stroke-width="2.4" />
                <span>{{ item }}</span>
              </li>
            </ul>
          </aside>
        </div>
      </section>

      <section id="testimonials" class="section">
        <div class="container">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--testimonials">Testimonials</span>
            <h2>Trusted by Teams Running Research, Verification, and Account Operations.</h2>
          </div>

          <div class="testimonial-grid">
            <article v-for="quote in testimonials" :key="quote.company" class="testimonial-card">
              <div class="testimonial-card__rating" aria-label="Five-star review">
                <span v-for="star in 5" :key="star" aria-hidden="true">★</span>
              </div>
              <p class="testimonial-card__quote" :class="{ 'is-placeholder': isPlaceholder(quote.quote) }">
                "{{ quote.quote }}"
              </p>
              <div class="testimonial-card__footer">
                <img class="testimonial-card__avatar" :src="quote.avatar" :alt="`${quote.author} avatar`" />
                <span>
                  <p class="testimonial-card__author" :class="{ 'is-placeholder': isPlaceholder(quote.author) }">
                    {{ quote.author }}
                  </p>
                  <p class="testimonial-card__meta" :class="{ 'is-placeholder': isPlaceholder(quote.company) }">
                    {{ quote.company }}
                  </p>
                </span>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section id="compliance" class="section section--alt compliance-section">
        <div class="container">
          <div class="compliance-panel">
            <div class="compliance-panel__primary">
              <span class="section-label section-label--compliance">Compliance / Security</span>
              <h2>Security Signals Buyers Can Verify Before Rollout.</h2>
              <p>
                Enterprise teams can request security documentation, privacy terms, and sourcing
                details during procurement review.
              </p>
            </div>

            <div class="compliance-strip" aria-label="Compliance and security signals">
              <div class="compliance-icon-grid">
                <article
                  v-for="cert in complianceCertifications"
                  :key="cert.label"
                  class="compliance-icon-card"
                  :class="`compliance-icon-card--${cert.tone}`"
                >
                  <span class="compliance-icon-card__mark" aria-hidden="true">
                    <span class="compliance-icon-card__short">{{ cert.short }}</span>
                  </span>
                  <span class="compliance-icon-card__label">{{ cert.label }}</span>
                </article>
              </div>
              <p class="compliance-strip__copy">
                Ethically sourced IPs with security documentation available on request.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section id="faq" class="section faq-section">
        <div class="container faq-wrap">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--faq">FAQ</span>
            <h2>Questions Buyers Ask Before Rollout.</h2>
          </div>

          <div class="faq-list">
            <details
              v-for="(item, index) in faqItems"
              :key="item.question"
              class="faq-item"
              :open="openFaqIndex === index"
            >
              <summary @click.prevent="openFaq(index)">
                <span>{{ item.question }}</span>
              </summary>
              <p>{{ item.answer }}</p>
            </details>
          </div>
        </div>
      </section>

      <section class="final-cta">
        <div class="container final-cta__inner">
          <span class="section-label section-label--dark section-label--ready">Ready to Launch</span>
          <h2>Start with <span class="grad-text grad-text--dark">Verified Proof Points</span>, Then Scale with Confidence.</h2>
          <p>
            Start with a stable ISP proxy setup for long-session workflows, then scale your
            coverage, routing rules, and support model as demand grows.
          </p>
          <div class="final-cta__actions">
            <a class="button button--primary button--large" href="#pricing">Start Free Trial</a>
            <a class="button button--dark-outline button--large" href="#faq">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import {
  BadgeCheck,
  Bot,
  CheckCircle2,
  Clock3,
  Code2,
  Copy,
  Database,
  DollarSign,
  Globe2,
  Headphones,
  KeyRound,
  Megaphone,
  PlugZap,
  Route,
  ScanSearch,
  Search,
  ServerCog,
  Shield,
  ShieldCheck,
  ShoppingBag,
  Smartphone,
  TerminalSquare,
  Zap,
} from '@lucide/vue'
import brandLogo from './assets-rola-logo.svg'
import capterraLogo from './assets/brand-icons/capterra.svg'
import curlLogo from './assets/brand-icons/curl.svg'
import g2Logo from './assets/brand-icons/g2.svg'
import nodeLogo from './assets/brand-icons/nodejs.svg'
import pythonLogo from './assets/brand-icons/python.svg'
import trustpilotLogo from './assets/brand-icons/trustpilot.svg'
import HeroParticles from './components/HeroParticles.vue'

gsap.registerPlugin(ScrollTrigger)

const pageRoot = ref<HTMLElement | null>(null)
const isHeaderScrolled = ref(false)
const currentPath = ref(window.location.pathname)
const currentHash = ref(window.location.hash)
const isUseCasesPage = computed(() => currentPath.value === '/use-cases')
const isPricingPage = computed(() => currentPath.value === '/pricing')
const isLightHeaderPage = computed(() => isUseCasesPage.value || isPricingPage.value)
let scrollAnimationContext: ReturnType<typeof gsap.context> | undefined
let handleHeaderScroll: (() => void) | undefined
let handleLocationChange: (() => void) | undefined
let proofCarouselTimer: number | undefined
const activeScrapingTestimonialIndex = ref(0)

const visibleScrapingTestimonials = computed(() => {
  return [0, 1, 2].map((offset) => ({
    ...scrapingTestimonials[(activeScrapingTestimonialIndex.value + offset) % scrapingTestimonials.length],
    slot: offset,
  }))
})

const displayedScrapingUseCases = computed(() => {
  return [
    ...scrapingUseCases.slice(0, 5),
    scrapingUseCases[5],
    scrapingUseCases[7],
  ]
})

onMounted(() => {
  handleLocationChange = () => {
    currentPath.value = window.location.pathname
    currentHash.value = window.location.hash
  }
  handleLocationChange()
  window.addEventListener('hashchange', handleLocationChange)
  window.addEventListener('popstate', handleLocationChange)

  handleHeaderScroll = () => {
    isHeaderScrolled.value = window.scrollY > 16
  }
  handleHeaderScroll()
  window.addEventListener('scroll', handleHeaderScroll, { passive: true })

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  if (isUseCasesPage.value && !prefersReducedMotion) {
    proofCarouselTimer = window.setInterval(() => {
      activeScrapingTestimonialIndex.value = (activeScrapingTestimonialIndex.value + 1) % scrapingTestimonials.length
    }, 6000)
  }

  if (!pageRoot.value || prefersReducedMotion) {
    return
  }

  scrollAnimationContext = gsap.context(() => {
    const animatedSelectors = [
      '.hero-demo',
      '.proof-panel',
      '.performance-card',
      '.pricing-card',
      '.coverage-card',
      '.feature-card',
      '.use-case-card',
      '.quick-start-card',
      '.testimonial-card',
      '.compliance-panel',
      '.scraping-challenge-card',
      '.scraping-capability-card',
      '.proxy-type-card',
      '.use-cases-page-card',
      '.scraping-compliance-panel',
      '.scraping-proof-card',
      '.faq-item',
    ]
    const animatedElements = animatedSelectors.flatMap((selector) =>
      Array.from(document.querySelectorAll<HTMLElement>(selector)),
    )

    gsap.set(animatedElements, { willChange: 'transform, opacity' })

    if (document.querySelector('.hero') && document.querySelector('.hero-demo')) {
      gsap.to('.hero-demo', {
        yPercent: 7,
        ease: 'none',
        scrollTrigger: {
          trigger: '.hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 0.8,
        },
      })
    }

    if (document.querySelector('.hero') && document.querySelector('.hero__content')) {
      gsap.to('.hero__content', {
        yPercent: -3,
        ease: 'none',
        scrollTrigger: {
          trigger: '.hero',
          start: 'top top',
          end: 'bottom top',
          scrub: 0.9,
        },
      })
    }

    gsap.utils
      .toArray<HTMLElement>(
        '.proof-panel, .performance-layout, .pricing-card, .coverage-card, .network-card, .quick-start-card, .feature-card, .testimonial-card, .compliance-panel, .scraping-challenge-card, .scraping-capability-card, .proxy-type-card, .use-cases-page-card, .scraping-compliance-panel, .scraping-proof-card, .faq-item',
      )
      .forEach((element) => {
        gsap.from(element, {
          autoAlpha: 0,
          y: 26,
          duration: 0.75,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: element,
            start: 'top 86%',
            once: true,
          },
        })
      })

    if (document.querySelector('.performance-section') && document.querySelector('.performance-card-grid')) {
      gsap.to('.performance-card-grid', {
        y: -30,
        ease: 'none',
        scrollTrigger: {
          trigger: '.performance-section',
          start: 'top bottom',
          end: 'bottom top',
          scrub: 1,
        },
      })
    }

  }, pageRoot.value)
})

onUnmounted(() => {
  if (handleHeaderScroll) {
    window.removeEventListener('scroll', handleHeaderScroll)
  }
  if (handleLocationChange) {
    window.removeEventListener('hashchange', handleLocationChange)
    window.removeEventListener('popstate', handleLocationChange)
  }
  scrollAnimationContext?.revert()
  if (proofCarouselTimer) {
    window.clearInterval(proofCarouselTimer)
  }
})

const navItems = [
  { label: 'Service', href: '/' },
  { label: 'Features', href: '/use-cases' },
  { label: 'Pricing', href: '/pricing' },
  { label: 'Coverage', href: '/#coverage' },
  { label: 'FAQ', href: '/#faq' },
]

const isNavItemActive = (item: (typeof navItems)[number]) => {
  if (item.href === '/') {
    return currentPath.value === '/' && !currentHash.value
  }

  if (item.href.startsWith('/#')) {
    return currentPath.value === '/' && currentHash.value === item.href.slice(1)
  }

  return currentPath.value === item.href
}

const heroMeta = [
  'Sticky sessions for longer workflows',
  'Per-IP pricing with no surprise bandwidth math',
]

const heroCardFields = [
  { label: 'Country', value: 'United States' },
  { label: 'Network Type', value: 'ISP Static' },
  { label: 'Session Duration', value: 'Up to 24h' },
  { label: 'Success Rate', value: '99.9%' },
]

const trustItems = [
  { logo: g2Logo, alt: 'G2', source: 'Reviewed on G2', value: '4.7/5', label: 'High-Intent Buyer Rating' },
  {
    logo: trustpilotLogo,
    alt: 'Trustpilot',
    source: 'Trustpilot Reviews',
    value: '4.6/5',
    label: 'Customer Satisfaction',
  },
  {
    logo: capterraLogo,
    alt: 'Capterra',
    source: 'Capterra Reviews',
    value: '4.5/5',
    label: 'Software Review Score',
  },
  { source: 'Trusted by Teams', value: '20,000+', label: 'Research and Automation Users' },
]

const stats = [
  { value: '99.9%', label: 'Success Rate on Fragile Targets', icon: Zap },
  { value: '1.3M+', label: 'ISP IP Pool Size', icon: Database },
  { value: 'From $1.30/IP', label: 'Starting Price per IP', icon: DollarSign },
  { value: '195+', label: 'Countries Covered', icon: Globe2 },
]

const socialAvatars = [
  'https://api.dicebear.com/10.x/notionists/svg?seed=Maya%20Chen&backgroundColor=ffffff&radius=50',
  'https://api.dicebear.com/10.x/notionists/svg?seed=Owen%20Park&backgroundColor=ffffff&radius=50',
  'https://api.dicebear.com/10.x/notionists/svg?seed=Priya%20Nair&backgroundColor=ffffff&radius=50',
  'https://api.dicebear.com/10.x/notionists/svg?seed=Daniel%20Reyes&backgroundColor=ffffff&radius=50',
]

const features = [
  {
    kicker: '01',
    category: 'Session Control',
    icon: Clock3,
    title: 'Sticky Sessions That Survive Longer Flows',
    description:
      'Keep the same identity across login-heavy tasks, account warm-up, and workflows that break when rotation happens too early.',
    metric: '24h',
    metricLabel: 'Sticky Session Window',
  },
  {
    kicker: '02',
    category: 'Network Trust',
    icon: ShieldCheck,
    title: 'Residential Trust with Cleaner Operational Framing',
    description:
      'Use ISP-assigned static identities that look closer to residential access patterns while staying easier to operate at scale.',
    metric: 'ISP',
    metricLabel: 'Static Residential Identity',
  },
  {
    kicker: '03',
    category: 'Billing Clarity',
    icon: DollarSign,
    title: 'Per-IP Packaging Buyers Can Understand Quickly',
    description:
      'This is easier to compare than per-GB pricing when the real concern is continuity, not burst traffic.',
    metric: '$1.30',
    metricLabel: 'Entry Price per IP',
  },
  {
    kicker: '04',
    category: 'Proof Layer',
    icon: BadgeCheck,
    title: 'Proof Points Buyers Can Verify Without Digging',
    description:
      'Put the numbers that matter up front: pool size, countries, success rate, and routing controls before a buyer asks sales.',
    metric: '99.9%',
    metricLabel: 'Published Success Rate',
  },
]

const performanceCards = [
  {
    label: 'Higher Session ROI',
    icon: BadgeCheck,
    value: '99.9%',
    description: 'Published success rate across fragile, stateful workflows.',
  },
  {
    label: 'Longer Continuity',
    icon: Clock3,
    value: '24h',
    description: 'Sticky session windows for account-sensitive operations.',
  },
  {
    label: 'Cleaner Pricing',
    icon: DollarSign,
    value: '$1.30',
    description: 'Entry price per IP for predictable team scaling.',
  },
]

const pricingPlans = [
  {
    name: 'Starter',
    icon: KeyRound,
    ipCount: '10 IPs',
    price: '$1.80/IP',
    items: ['Location access', 'Dashboard access', 'Email support'],
    cta: 'Start Trial',
    featured: false,
  },
  {
    name: 'Advanced',
    icon: Route,
    ipCount: '100 IPs',
    price: '$1.50/IP',
    items: ['More IP inventory', 'Priority routing', '24/7 support'],
    cta: 'Choose Plan',
    featured: false,
  },
  {
    name: 'Premium',
    icon: Headphones,
    ipCount: '500 IPs',
    price: '$1.30/IP',
    items: ['Dedicated onboarding', 'Broader geo access', 'Account manager'],
    cta: 'Choose Plan',
    featured: true,
  },
  {
    name: 'Enterprise',
    icon: ServerCog,
    ipCount: '2,000+ IPs',
    price: 'Custom Pricing',
    items: ['Custom sourcing strategy', 'Security review support', 'Commercial terms'],
    cta: 'Talk to Sales',
    featured: false,
  },
]

const pricingPageMetrics = [
  { icon: Database, value: '1.3M+', label: 'ISP and residential IPs' },
  { icon: BadgeCheck, value: '99.9%', label: 'Published success rate' },
  { icon: Globe2, value: '195+', label: 'Countries and regions' },
  { icon: Clock3, value: '24h', label: 'Sticky session window' },
]

const pricingPagePlans = [
  {
    name: 'Starter',
    icon: KeyRound,
    fit: 'Validate one workflow',
    ipCount: '10 IPs',
    price: '$1.80/IP',
    monthly: '$18 monthly package',
    items: ['Country routing', 'Dashboard access', 'Email support'],
    cta: 'Start Trial',
    featured: false,
  },
  {
    name: 'Advanced',
    icon: Route,
    fit: 'Scale a repeatable run',
    ipCount: '100 IPs',
    price: '$1.50/IP',
    monthly: '$150 monthly package',
    items: ['Larger IP inventory', 'Priority routing', '24/7 support'],
    cta: 'Choose Plan',
    featured: false,
  },
  {
    name: 'Premium',
    icon: Headphones,
    fit: 'Production rollout',
    ipCount: '500 IPs',
    price: '$1.30/IP',
    monthly: '$650 monthly package',
    items: ['Dedicated onboarding', 'Broader geo access', 'Account manager'],
    cta: 'Choose Plan',
    featured: true,
  },
  {
    name: 'Enterprise',
    icon: ServerCog,
    fit: 'Custom procurement',
    ipCount: '2,000+ IPs',
    price: 'Custom Pricing',
    monthly: 'Routing and sourcing review',
    items: ['Custom sourcing strategy', 'Security review support', 'Commercial terms'],
    cta: 'Talk to Sales',
    featured: false,
  },
]

const pricingPageNotes = [
  'VAT or local tax may apply by billing location',
  'Bandwidth policy is confirmed before checkout',
  'Enterprise terms available after routing review',
]

const pricingPlanIncludes = [
  {
    title: 'HTTP(S) and SOCKS5',
    description: 'Use standard proxy protocols across browsers, scrapers, and internal tools.',
  },
  {
    title: 'Country-level routing',
    description: 'Route by priority market, with deeper availability review for larger allocations.',
  },
  {
    title: 'Sticky sessions',
    description: 'Keep the same identity active for workflows that need continuity across steps.',
  },
  {
    title: 'Dashboard visibility',
    description: 'Monitor allocation, routing choices, and usage context before scaling.',
  },
  {
    title: 'Usage boundaries',
    description: 'Acceptable-use review helps keep sensitive workflows inside clear rules.',
  },
  {
    title: 'Support path',
    description: 'Get setup help, routing review, and procurement support as plans grow.',
  },
]

const pricingBillingCards = [
  {
    icon: DollarSign,
    title: 'Predictable per-IP math',
    description: 'Forecast cost from inventory size instead of translating every workflow into bandwidth estimates.',
  },
  {
    icon: Clock3,
    title: 'Start small, then scale',
    description: 'Validate one route and session pattern before moving into larger regional allocations.',
  },
  {
    icon: ShieldCheck,
    title: 'Review before commitment',
    description: 'Custom and sensitive workflows can go through sourcing, compliance, and traffic review first.',
  },
]

const pricingCapabilities = [
  {
    icon: Database,
    title: 'Large ISP Pool',
    description: 'Access a broad static ISP and residential pool for commercial research and verification workflows.',
  },
  {
    icon: KeyRound,
    title: 'Session Control',
    description: 'Pin sticky sessions for login-heavy, stateful, or multi-step automation paths.',
  },
  {
    icon: Shield,
    title: 'Lower Block Risk',
    description: 'Use residential-grade trust signals where datacenter routes create too much friction.',
  },
  {
    icon: Zap,
    title: 'Fewer Retry Loops',
    description: 'Stable identity helps reduce wasted retries when target context must stay consistent.',
  },
  {
    icon: Globe2,
    title: 'Global Coverage',
    description: 'Plan market-specific checks across 195+ countries and priority commercial regions.',
  },
  {
    icon: Headphones,
    title: 'Support for Scale',
    description: 'Premium and enterprise packages add onboarding, routing review, and account management.',
  },
]

const pricingReviewSignals = [
  { logo: g2Logo, alt: 'G2', value: '4.7/5', label: 'High-intent buyer rating' },
  { logo: trustpilotLogo, alt: 'Trustpilot', value: '4.6/5', label: 'Customer satisfaction' },
  { logo: capterraLogo, alt: 'Capterra', value: '4.5/5', label: 'Software review score' },
]

const pricingTestimonials = [
  {
    quote:
      'The per-IP model made pricing easier to explain internally because the cost followed the number of stable identities we needed.',
    author: 'Daniel Reyes, Growth Systems Manager',
  },
  {
    quote:
      'We could start with a small allocation, validate country routing, and expand without changing the integration pattern.',
    author: 'Maya Chen, Data Operations Lead',
  },
]

const pricingSecurityItems = [
  {
    icon: ShieldCheck,
    title: 'Secure checkout review',
    description: 'Confirm plan, billing location, and usage expectations before payment or procurement.',
  },
  {
    icon: BadgeCheck,
    title: 'Sourcing documentation',
    description: 'Enterprise buyers can request sourcing, privacy, and security materials during review.',
  },
  {
    icon: DollarSign,
    title: 'Invoice support',
    description: 'Larger deployments can discuss commercial terms, invoices, and custom procurement needs.',
  },
  {
    icon: Headphones,
    title: 'Onboarding support',
    description: 'Premium and enterprise teams get setup review for sensitive or high-value workflows.',
  },
]

const pricingPageFaqItems = [
  {
    question: 'Is this pricing per IP or per GB?',
    answer:
      'This page prices static ISP proxy packages per IP. That fits workflows where stable identities and session continuity matter more than raw bandwidth volume.',
  },
  {
    question: 'Can I start without a large monthly commitment?',
    answer:
      'Yes. Starter is designed for validation before a team moves into Advanced, Premium, or custom enterprise inventory.',
  },
  {
    question: 'Does bandwidth change the listed package price?',
    answer:
      'The visible package price is based on IP inventory. Bandwidth policy and unusually high-volume workflows should be confirmed before checkout or procurement approval.',
  },
  {
    question: 'Can I upgrade in the middle of a rollout?',
    answer:
      'Teams can expand from a smaller package to a larger allocation after routing, session behavior, and target compatibility are validated.',
  },
  {
    question: 'What payment or procurement options are available?',
    answer:
      'Self-serve and enterprise procurement needs are handled by plan. Larger deployments can request invoice, sourcing, security, and commercial documentation.',
  },
  {
    question: 'Do you require compliance review or KYC?',
    answer:
      'Enterprise and sensitive workflows may require additional review. Rola-IP is intended for legitimate research, monitoring, verification, and automation use cases.',
  },
  {
    question: 'Are there restricted targets or use cases?',
    answer:
      'Yes. Fraud, spam, credential abuse, and high-risk account manipulation are not allowed. Teams should validate target policies before production rollout.',
  },
  {
    question: 'Is there a free trial or money-back policy?',
    answer:
      'Teams can start with a small ISP proxy allocation to validate fit. Any trial scope or refund terms should be confirmed before checkout.',
  },
]

const coverageSummary = '195+ Countries'

const coverage = [
  { flag: '🇺🇸', name: 'United States', count: '5.4M+ IPs' },
  { flag: '🇬🇧', name: 'United Kingdom', count: '110K+ IPs' },
  { flag: '🇩🇪', name: 'Germany', count: '376K+ IPs' },
  { flag: '🇫🇷', name: 'France', count: '190K+ IPs' },
  { flag: '🇨🇦', name: 'Canada', count: '320K+ IPs' },
  { flag: '🇦🇺', name: 'Australia', count: '95K+ IPs' },
]

const useCases = [
  {
    icon: ShoppingBag,
    title: 'E-commerce Intelligence',
    description:
      'Track listings, pricing, seller behavior, and storefront changes with more continuity across repeated collection sessions.',
    signal: 'Stable storefront reads',
  },
  {
    icon: Megaphone,
    title: 'Ad Verification',
    description:
      'Validate regional delivery, landing page behavior, and account-specific ad flows from trusted static identities.',
    signal: 'Geo-accurate ad paths',
  },
  {
    icon: Search,
    title: 'Market Research',
    description:
      'Collect location-sensitive pricing and catalog signals without the churn that often comes with aggressive rotation.',
    signal: 'Cleaner market snapshots',
  },
  {
    icon: Shield,
    title: 'Cybersecurity Operations',
    description:
      'Audit abuse surfaces, monitor impersonation, and test sensitive account flows with believable, persistent sessions.',
    signal: 'Persistent audit identity',
  },
  {
    icon: ScanSearch,
    title: 'SEO and SERP Monitoring',
    description:
      'Check rankings and localized results more consistently when your workflow relies on stable market identity.',
    signal: 'Localized SERP checks',
  },
  {
    icon: Bot,
    title: 'AI Data Collection',
    description:
      'Support longer authenticated collection jobs that need trust, continuity, and fewer avoidable interruptions.',
    signal: 'Long-running data jobs',
  },
]

const scrapingHeroStats = [
  { value: '1.3M+', label: 'ISP and residential IPs' },
  { value: '99.9%', label: 'target success benchmark' },
  { value: '195+', label: 'countries and regions' },
]

const scrapingHeroJobs = [
  { label: 'Requests', value: '42.8K' },
  { label: 'Clean reads', value: '99.1%' },
  { label: 'Avg latency', value: '0.62s' },
]

const scrapingHeroTimeline = [
  { label: 'Mon', height: '42%' },
  { label: 'Tue', height: '68%' },
  { label: 'Wed', height: '54%' },
  { label: 'Thu', height: '82%' },
  { label: 'Fri', height: '74%' },
  { label: 'Sat', height: '61%' },
]

const scrapingChallengeSignals = [
  { label: 'Blocks', height: '64%' },
  { label: 'CAPTCHA', height: '42%' },
  { label: 'Geo drift', height: '72%' },
  { label: 'Retries', height: '51%' },
  { label: 'Cost', height: '58%' },
]

const scrapingChallengeMeta = [
  { value: '2.8x', label: 'retry cost spike' },
  { value: '37%', label: 'noisy market reads' },
  { value: '24h', label: 'sticky session need' },
]

const scrapingChallenges = [
  {
    icon: Bot,
    title: 'Bot Detection and IP Bans',
    description:
      'Automated traffic is easier to flag when too many requests come from reused, low-trust, or poorly routed IPs.',
  },
  {
    icon: Globe2,
    title: 'Geo Restrictions and Market Drift',
    description:
      'Prices, rankings, ads, and inventory often change by country or city, so unstable location context creates noisy data.',
  },
  {
    icon: Shield,
    title: 'CAPTCHA, Rate Limits, and WAFs',
    description:
      'CAPTCHA loops, throttling, and web application firewalls can turn simple scraping jobs into expensive retry systems.',
  },
  {
    icon: ServerCog,
    title: 'High Maintenance Cost',
    description:
      'Engineering teams lose time maintaining proxy pools, retry logic, browser settings, and target-specific exceptions.',
  },
]

const scrapingCapabilities = [
  {
    icon: ShieldCheck,
    metric: 'Low bans',
    title: 'Higher Success with Trusted IPs',
    description:
      'Use residential-grade and ISP-backed identities to reduce suspicious traffic signals on fragile public targets.',
  },
  {
    icon: Route,
    metric: 'Rotate',
    title: 'Large Pool with Rotation Control',
    description:
      'Rotate across a broader pool when reach matters, or keep a session stable when the workflow depends on continuity.',
  },
  {
    icon: Globe2,
    metric: '195+',
    title: 'Global Geo Targeting',
    description:
      'Route collectors by country and region so pricing, search results, ads, and availability stay market-specific.',
  },
  {
    icon: Clock3,
    metric: 'Sticky',
    title: 'Session Control for Stateful Targets',
    description:
      'Switch between rotating and sticky sessions for websites that need persistent identity across multi-step flows.',
  },
  {
    icon: Code2,
    metric: 'Fast setup',
    title: 'Works with Existing Scraping Stacks',
    description:
      'Connect through standard proxy auth in curl, Python, Node, browser automation, or internal data collection runners.',
  },
  {
    icon: BadgeCheck,
    metric: 'Review-ready',
    title: 'Cleaner Enterprise Rollout',
    description:
      'Support legitimate public data workflows with clearer sourcing, usage boundaries, and security documentation.',
  },
]

const scrapingIntegrationCards = [
  { icon: Code2, name: 'Python requests', detail: 'Session route · US market', muted: false },
  { icon: ScanSearch, name: 'Playwright', detail: 'Browser collector · sticky', muted: false },
  { icon: Route, name: 'Scrapy', detail: 'Queue worker · rotating', muted: false },
  { icon: TerminalSquare, name: 'Puppeteer', detail: 'JS render · retry rules', muted: true },
]

const routingDiagnostics = [
  { label: 'US ISP static', value: 'Healthy', fill: '96%' },
  { label: 'CAPTCHA retry', value: 'Low', fill: '18%' },
  { label: 'Session drift', value: 'Stable', fill: '88%' },
]

const scrapingProxyFit = [
  {
    icon: ShieldCheck,
    type: 'Residential',
    fit: 'Anti-blocking and broad public web collection',
    note: 'Best when target trust matters more than raw speed.',
    price: 'See residential plans',
  },
  {
    icon: KeyRound,
    type: 'ISP / Static Residential',
    fit: 'Longer scraping sessions with stable identity',
    note: 'Best for logged-in, stateful, or repeated regional checks.',
    price: 'See ISP plans',
  },
  {
    icon: Zap,
    type: 'Datacenter',
    fit: 'Speed and cost-sensitive scraping',
    note: 'Best for lower-risk targets where trust signals matter less.',
    price: 'Speed-first option',
  },
  {
    icon: Smartphone,
    type: 'Mobile',
    fit: 'Mobile content, app views, and hyper-local checks',
    note: 'Best when the target behaves differently on mobile networks.',
    price: 'Mobile fit check',
  },
]

const scrapingUseCases = [
  {
    icon: ShoppingBag,
    title: 'E-commerce Price Intelligence',
    description:
      'Monitor products, seller changes, stock status, and regional prices with stable identities across repeated collection windows.',
    signal: 'Price and catalog monitoring',
  },
  {
    icon: ScanSearch,
    title: 'SEO and SERP Tracking',
    description:
      'Collect localized ranking snapshots without mixing market context across requests or losing continuity mid-check.',
    signal: 'Localized search snapshots',
  },
  {
    icon: Bot,
    title: 'AI and LLM Training Data',
    description:
      'Support longer collection jobs for public web datasets where retry quality, regional diversity, and consistency matter.',
    signal: 'Training data collection',
  },
  {
    icon: Megaphone,
    title: 'Ad Verification',
    description:
      'Validate regional delivery, landing pages, and account-specific ad paths from trusted static residential identities.',
    signal: 'Geo-accurate ad paths',
  },
  {
    icon: Search,
    title: 'Market Research',
    description:
      'Collect competitive pricing, inventory, and marketplace signals while reducing noise from aggressive IP rotation.',
    signal: 'Cleaner market snapshots',
  },
  {
    icon: Shield,
    title: 'Cybersecurity Research',
    description:
      'Audit impersonation, abuse surfaces, and sensitive account flows with persistent identities that fit review workflows.',
    signal: 'Persistent audit identity',
  },
  {
    icon: Globe2,
    title: 'Travel Data Collection',
    description:
      'Track fares, hotel availability, regional offers, and booking flows from the markets your customers actually search from.',
    signal: 'Localized travel checks',
  },
  {
    icon: Clock3,
    title: 'Website Change Monitoring',
    description:
      'Detect page, price, policy, and availability changes with repeatable snapshots instead of one-off crawler successes.',
    signal: 'Repeatable change tracking',
  },
]

const scrapingQuickSteps = [
  {
    icon: Route,
    title: 'Pick Proxy Type and Market',
    description: 'Choose residential, ISP, datacenter, or mobile based on target risk and geo needs.',
  },
  {
    icon: KeyRound,
    title: 'Create Auth and Session Rules',
    description: 'Generate credentials, country routing, and sticky-session keys for the crawler.',
  },
  {
    icon: Search,
    title: 'Connect and Monitor Results',
    description: 'Plug the endpoint into your scraper, then tune rotation, retries, and target coverage.',
  },
]

const scrapingTools = ['Scrapy', 'Puppeteer', 'Playwright', 'Selenium', 'Octoparse', 'Python requests']

const scrapingTestimonials = [
  {
    quote:
      'Stable sessions made our price monitoring jobs easier to audit because the market context stopped changing halfway through a run.',
    author: 'Maya Chen',
    role: 'Data Operations Lead',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Maya%20Chen&backgroundColor=ffffff&radius=50',
  },
  {
    quote:
      'The biggest win was reducing maintenance noise. Our team could tune target logic instead of constantly rebuilding proxy retries.',
    author: 'Daniel Reyes',
    role: 'Growth Systems Manager',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Daniel%20Reyes&backgroundColor=ffffff&radius=50',
  },
  {
    quote:
      'We could compare regional listings with fewer false changes because routing stayed predictable across each collection window.',
    author: 'Olivia Hart',
    role: 'Market Intelligence Manager',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Olivia%20Hart&backgroundColor=ffffff&radius=50',
  },
  {
    quote:
      'Our crawler team stopped treating proxy retries as a black box. Session rules became part of rollout planning instead.',
    author: 'Ethan Brooks',
    role: 'Automation Engineering Lead',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Ethan%20Brooks&backgroundColor=ffffff&radius=50',
  },
]

const scrapingAwards = ['G2 review signals', 'Trustpilot rating', 'Enterprise onboarding', 'Security documentation']

const scrapingFaqItems = [
  {
    question: 'Should a web scraping workflow use ISP proxies or rotating residential proxies?',
    answer:
      'Use ISP proxies when the workflow depends on stable sessions, repeated regional checks, account state, or cleaner before-and-after comparisons. Use rotating residential proxies when each request can safely use a different identity.',
  },
  {
    question: 'Can I target a specific country or city?',
    answer:
      'Country-level routing is supported for broad market checks. City-level or ASN-level availability depends on inventory and should be validated before production rollout.',
  },
  {
    question: 'Can I use this with my existing scraper or browser automation stack?',
    answer:
      'Yes. The integration works through standard proxy authentication and session headers, so teams can connect curl, Python, Node, Playwright, Puppeteer, Scrapy, or internal collectors without rebuilding the whole pipeline.',
  },
  {
    question: 'My scraper got blocked. What should I change first?',
    answer:
      'Start by reducing request bursts, checking headers and browser behavior, switching proxy type, and deciding whether the target needs rotation or a longer sticky session.',
  },
  {
    question: 'Is web scraping legal?',
    answer:
      'Web scraping rules depend on the target, data type, jurisdiction, and collection method. Rola-IP is intended for legitimate public data research, monitoring, and verification, and teams should review policies before rollout.',
  },
  {
    question: 'Which scraping scenarios benefit most from sticky ISP sessions?',
    answer:
      'E-commerce price intelligence, SEO and SERP tracking, ad verification, AI dataset collection, brand monitoring, and account-sensitive research often benefit from stable identity and predictable routing.',
  },
  {
    question: 'Do you provide a managed Web Scraping API?',
    answer:
      'This page currently focuses on proxy-based scraping workflows. If a managed scraping or Web Data API is added, it should become a dedicated product path with rendering, retries, and structured output clearly defined.',
  },
]

const networkSignals = [
  {
    kicker: 'Session policy',
    icon: KeyRound,
    title: 'Pin Identity for the Workflows That Cannot Afford Churn.',
    description:
      'Keep a single ISP identity active for up to 24 hours across account state, verification paths, and long-running research jobs.',
  },
  {
    kicker: 'Routing control',
    icon: Route,
    title: 'Map Country, Session, and Plan Rules Before Requests Leave Your Stack.',
    description:
      'Route by country, plan tier, and sticky-session key across 195+ markets without rebuilding endpoint logic.',
  },
  {
    kicker: 'Support layer',
    icon: Headphones,
    title: 'Make Escalation Paths Clear for Enterprise Teams.',
    description:
      'Premium and enterprise plans include 24/7 technical support, dedicated onboarding, and traffic review for sensitive workflows.',
  },
]

const codeSamples = {
  curl: `$ curl -x http://username:password@gateway.rola-ip.com:port \\
  -H "X-Session-ID: sticky-session-01" \\
  "https://target.example.com"

# Country: US | Session TTL: 24h | Avg latency: 0.58s
# Pool: ISP Static | Auth: username/password`,
  node: `import { request } from "undici"

const proxy = "http://username:password@gateway.rola-ip.com:port"
const session = "sticky-session-01"

await request("https://target.example.com", {
  dispatcher: buildRolaProxy(proxy, session),
})`,
  python: `import requests

proxies = {
    "https": "http://username:password@gateway.rola-ip.com:port"
}
headers = {"X-Session-ID": "sticky-session-01"}

requests.get("https://target.example.com", proxies=proxies, headers=headers)`,
} as const

type CodeTabKey = keyof typeof codeSamples

const codeTabs: Array<{ key: CodeTabKey; label: string; logo: string }> = [
  { key: 'curl', label: 'curl', logo: curlLogo },
  { key: 'node', label: 'node', logo: nodeLogo },
  { key: 'python', label: 'python', logo: pythonLogo },
]

const hasCopiedCode = ref(false)
const openFaqIndex = ref(0)
const openUseCaseFaqIndex = ref(0)
const openPricingPageFaqIndex = ref(0)
const activeCodeTab = ref<CodeTabKey>('curl')

const activeCodeSample = computed(() => codeSamples[activeCodeTab.value])

type CodeToken = {
  value: string
  kind: 'plain' | 'command' | 'keyword' | 'string' | 'endpoint' | 'session' | 'metric' | 'comment'
}

const codeTokenPatterns: Array<{ pattern: RegExp; kind: CodeToken['kind'] }> = [
  { pattern: /"https?:\/\/[^"]+"/g, kind: 'endpoint' },
  { pattern: /https?:\/\/[^\s"'}]+/g, kind: 'endpoint' },
  { pattern: /"X-Session-ID: sticky-session-01"/g, kind: 'session' },
  { pattern: /"sticky-session-01"/g, kind: 'session' },
  { pattern: /gateway\.rola-ip\.com:port/g, kind: 'endpoint' },
  { pattern: /sticky-session-01/g, kind: 'session' },
  { pattern: /\b(24h|0\.58s|US|ISP Static)\b/g, kind: 'metric' },
  { pattern: /\b(curl|import|from|const|await|requests|get|request|dispatcher|headers|proxies)\b/g, kind: 'keyword' },
  { pattern: /"[^"]*"/g, kind: 'string' },
  { pattern: /^\s*#.*$/g, kind: 'comment' },
  { pattern: /^\$\s*/g, kind: 'command' },
]

const tokenizeCodeLine = (line: string): CodeToken[] => {
  const matches = codeTokenPatterns.flatMap(({ pattern, kind }) =>
    Array.from(line.matchAll(pattern), (match) => ({
      start: match.index ?? 0,
      end: (match.index ?? 0) + match[0].length,
      value: match[0],
      kind,
    })),
  )

  const orderedMatches = matches
    .sort((a, b) => a.start - b.start || b.end - a.end)
    .filter((match, index, sorted) => !sorted.some((other, otherIndex) => otherIndex < index && match.start < other.end))

  const tokens: CodeToken[] = []
  let cursor = 0
  orderedMatches.forEach((match) => {
    if (match.start > cursor) {
      tokens.push({ value: line.slice(cursor, match.start), kind: 'plain' })
    }
    tokens.push({ value: match.value, kind: match.kind })
    cursor = match.end
  })

  if (cursor < line.length) {
    tokens.push({ value: line.slice(cursor), kind: 'plain' })
  }

  return tokens.length ? tokens : [{ value: ' ', kind: 'plain' }]
}

const codeSampleLines = computed(() =>
  activeCodeSample.value.split('\n').map((text, index) => ({
    number: String(index + 1).padStart(2, '0'),
    text: text || ' ',
    tokens: tokenizeCodeLine(text || ' '),
  })),
)

const copyCodeSample = async () => {
  hasCopiedCode.value = true
  window.setTimeout(() => {
    hasCopiedCode.value = false
  }, 1800)

  try {
    await navigator.clipboard.writeText(activeCodeSample.value)
  } catch {
    const textarea = document.createElement('textarea')
    textarea.value = activeCodeSample.value
    textarea.setAttribute('readonly', '')
    textarea.style.position = 'fixed'
    textarea.style.opacity = '0'
    textarea.style.pointerEvents = 'none'
    document.body.appendChild(textarea)
    textarea.focus()
    textarea.select()
    textarea.setSelectionRange(0, textarea.value.length)
    document.execCommand('copy')
    textarea.remove()
  }
}

const openFaq = (index: number) => {
  openFaqIndex.value = index
}

const openUseCaseFaq = (index: number) => {
  openUseCaseFaqIndex.value = index
}

const openPricingPageFaq = (index: number) => {
  openPricingPageFaqIndex.value = index
}

const quickStartItems = [
  {
    icon: TerminalSquare,
    title: 'Endpoint Generator',
    description:
      'Generate production-ready endpoints for country, city, session ID, and authentication in under 60 seconds.',
  },
  {
    icon: Code2,
    title: 'SDK and Language Examples',
    description:
      'Copy tested curl, Python, and Node snippets with the same sticky-session format used in the dashboard.',
  },
  {
    icon: PlugZap,
    title: 'Tool Integrations',
    description:
      'Connect quickly with browsers, scraping frameworks, ad verification tools, and internal automation runners.',
  },
]

const comparisonRows = [
  {
    label: 'Session Continuity',
    isp: 'Up to 24h sticky identity',
    rotating: 'Minutes to hours depending on pool rules',
    datacenter: 'Stable identity, lower trust signals',
  },
  {
    label: 'Commercial Framing',
    isp: 'From $1.30/IP with fixed inventory',
    rotating: 'Often priced by GB usage',
    datacenter: 'Low-cost IPs, higher block risk',
  },
  {
    label: 'Typical Workflow Fit',
    isp: 'Account operations, research, verification',
    rotating: 'Large-scale public web collection',
    datacenter: 'Speed-first internal or low-risk tasks',
  },
]

const explainBullets = [
  'Residential-grade trust signals with static ISP ownership.',
  'Predictable per-IP control for longer-running systems.',
  'Best for logged-in, stateful, or verification-heavy flows.',
]

const testimonials = [
  {
    quote:
      'Static ISP sessions helped us keep longer verification runs stable without constantly rebuilding workflows around rotation.',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Maya%20Chen&backgroundColor=b6e3f4',
    author: 'Maya Chen, Data Operations Lead',
    company: 'Market Intelligence Team',
  },
  {
    quote:
      'The per-IP model is easier for our team to forecast, and the country-level routing makes regional checks much simpler.',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Daniel%20Reyes&backgroundColor=c0aede',
    author: 'Daniel Reyes, Growth Systems Manager',
    company: 'Ad Verification Workflow',
  },
  {
    quote:
      'Onboarding felt practical: clear endpoints, stable sessions, and support that understood why continuity mattered.',
    avatar: 'https://api.dicebear.com/10.x/notionists/svg?seed=Priya%20Nair&backgroundColor=ffdfbf',
    author: 'Priya Nair, Automation Architect',
    company: 'E-commerce Research Team',
  },
]

const complianceCertifications = [
  { label: 'ISO 27001', short: 'ISO', tone: 'iso' },
  { label: 'SOC 2', short: 'SOC', tone: 'soc' },
  { label: 'GDPR', short: 'EU', tone: 'gdpr' },
  { label: 'CCPA', short: 'CA', tone: 'ccpa' },
]

const faqItems = [
  {
    question: 'What Is an ISP Proxy?',
    answer:
      'An ISP proxy is a static residential proxy hosted through an internet service provider. It combines residential trust signals with a more stable identity for workflows that need continuity.',
  },
  {
    question: 'How Is It Different from Rotating Residential Proxies?',
    answer:
      'Rotating residential proxies are useful when every request can use a different identity. ISP static proxies are better when login flows, carts, dashboards, or verification steps need the same IP for longer periods.',
  },
  {
    question: 'Is There a Free Trial?',
    answer:
      'Yes. Teams can start with a small ISP proxy allocation to validate routing, session behavior, and target compatibility before moving into a larger plan.',
  },
  {
    question: 'How Does Billing Work?',
    answer:
      'Plans are presented with predictable per-IP pricing, so teams can estimate monthly cost by inventory size rather than relying only on bandwidth consumption.',
  },
  {
    question: 'Which Locations Are Supported?',
    answer:
      'Rola-IP supports 195+ countries, with priority ISP inventory in the United States, United Kingdom, Germany, France, Canada, Australia, and other major commercial markets.',
  },
  {
    question: 'Are There Any Target Restrictions?',
    answer:
      'Yes. Access is designed for legitimate business workflows such as research, monitoring, verification, and automation. Fraud, spam, credential abuse, and high-risk account manipulation are not allowed.',
  },
  {
    question: 'How Long Can a Session Stay on One IP?',
    answer:
      'Sticky sessions can be configured for up to 24 hours, making them suitable for long-running research, verification, monitoring, and account-sensitive automation workflows.',
  },
  {
    question: 'What Compliance Standards Do You Support?',
    answer:
      'Enterprise customers can request security documentation, data-processing terms, sourcing information, and procurement questionnaire support during onboarding.',
  },
]

const isPlaceholder = (value: string) => value.startsWith('[')
</script>
