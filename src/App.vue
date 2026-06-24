<template>
  <div ref="pageRoot" class="site-page">
    <header class="site-header" :class="{ 'site-header--scrolled': isHeaderScrolled, 'site-header--use-cases': isLightHeaderPage }" aria-label="Primary">
      <div class="container site-header__inner">
        <a class="brand" href="/" aria-label="ROLA-IP home">
          <img class="brand__logo" :src="brandLogo" alt="ROLA-IP" />
        </a>

        <nav class="site-nav" aria-label="Section navigation">
          <div
            v-for="item in navItems"
            :key="item.label"
            class="site-nav__item"
            :class="{ 'site-nav__item--dropdown': item.dropdown }"
          >
            <a
              :href="item.href"
              class="site-nav__link"
              :aria-haspopup="item.dropdown ? 'true' : undefined"
            >
              {{ item.label }}
              <ChevronDown
                v-if="item.dropdown"
                class="site-nav__chevron"
                aria-hidden="true"
                :size="14"
                :stroke-width="2.4"
              />
            </a>

            <div v-if="item.dropdown === 'service'" class="service-menu" aria-label="Service proxy options">
              <div class="service-menu__panel service-menu__panel--products">
                <div class="service-menu__grid">
                  <a
                    v-for="option in serviceMenuItems"
                    :key="option.title"
                    :href="option.href"
                    class="service-menu__item"
                    :class="`service-menu__item--${option.group}`"
                  >
                    <span
                      class="service-menu__icon"
                      :class="[
                        `service-menu__icon--${option.tone}`,
                        `service-menu__icon--${option.group}`,
                      ]"
                    >
                      <span class="service-menu__glyph" aria-hidden="true" v-html="option.iconSvg"></span>
                    </span>
                    <span class="service-menu__copy">
                      <strong>{{ option.title }}</strong>
                      <small>{{ option.description }}</small>
                    </span>
                  </a>
                </div>
              </div>
            </div>

            <div v-else-if="item.dropdown === 'pricing'" class="service-menu pricing-menu" aria-label="Proxy pricing options">
              <div class="service-menu__panel pricing-menu__panel">
                <div class="pricing-menu__grid">
                  <a
                    v-for="option in pricingMenuItems"
                    :key="option.title"
                    :href="option.href"
                    class="pricing-menu__item"
                  >
                    <span
                      class="service-menu__icon"
                      :class="[
                        `service-menu__icon--${option.tone}`,
                        `service-menu__icon--${option.group}`,
                      ]"
                    >
                      <span class="service-menu__glyph" aria-hidden="true" v-html="option.iconSvg"></span>
                    </span>
                    <span class="service-menu__copy pricing-menu__copy">
                      <strong>{{ option.title }}</strong>
                      <small>{{ option.description }}</small>
                    </span>
                    <b class="pricing-menu__price" data-no-translate>{{ option.price }}</b>
                  </a>
                </div>
              </div>
            </div>

            <div v-else-if="item.dropdown === 'purposes'" class="purpose-menu" aria-label="Platform purpose options">
              <div class="purpose-menu__inner">
                <div v-for="(column, columnIndex) in purposeMenuColumns" :key="columnIndex" class="purpose-menu__column">
                  <section
                    v-for="section in column"
                    :key="section.title"
                    class="purpose-menu__section"
                    :class="{ 'purpose-menu__section--paired': section.paired }"
                  >
                    <a class="purpose-menu__heading" :href="section.href">
                      <span class="purpose-menu__heading-icon">
                        <component :is="section.icon" aria-hidden="true" :size="18" :stroke-width="2.25" />
                      </span>
                      <span>{{ section.title }}</span>
                    </a>
                    <div class="purpose-menu__links">
                      <a
                        v-for="platform in section.platforms"
                        :key="`${section.title}-${platform.name}`"
                      class="purpose-menu__platform"
                      :href="platform.href"
                    >
                      <span class="purpose-menu__logo">
                          <img :src="platform.icon" :alt="`${platform.name} logo`" loading="lazy" />
                      </span>
                      <span>{{ platform.name }}</span>
                    </a>
                    </div>
                  </section>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <div class="site-actions">
          <div class="language-select site-language site-language--top" data-language-select data-no-translate>
            <button
              type="button"
              class="language-select__trigger"
              :aria-label="languageSwitcherLabel"
              aria-haspopup="menu"
              :aria-expanded="isLanguageMenuOpen"
              @click="toggleLanguageMenu"
              @keydown.escape="closeLanguageMenu"
            >
              <img class="language-select__flag" :src="flagIcon(currentLanguage.flagCode)" alt="" aria-hidden="true" />
              <span>{{ currentLanguage.shortLabel }}</span>
              <ChevronDown aria-hidden="true" :size="14" :stroke-width="2.4" />
            </button>
            <div
              v-if="isLanguageMenuOpen"
              class="language-select__menu"
              role="menu"
              :aria-label="languageSwitcherLabel"
            >
              <button
                v-for="language in languageOptions"
                :key="language.code"
                type="button"
                class="language-select__option"
                :class="{ 'language-select__option--active': currentLocale === language.code }"
                role="menuitemradio"
                :aria-checked="currentLocale === language.code"
                @click="setLocale(language.code)"
              >
                <img class="language-select__flag" :src="flagIcon(language.flagCode)" alt="" aria-hidden="true" />
                <span>{{ language.nativeLabel }}</span>
                <small>{{ language.shortLabel }}</small>
              </button>
            </div>
          </div>
          <a class="button button--primary" href="https://console.rola-ip.co/login">Log in / Sign up</a>
        </div>
      </div>
    </header>

    <main v-if="isHomePage" id="top" class="home-page">
      <section class="home-hero">
        <HomeHeroShader />
        <div class="container home-hero__grid">
          <div class="home-hero__copy">
            <h1>Reliable Data Collection Solutions for Your Business.</h1>
            <p>
              Build stable proxy workflows for web data, market intelligence, automation, and
              account operations with static ISP sessions designed for business teams.
            </p>
            <div class="home-hero__actions">
              <a class="button button--primary button--large" href="/service">
                Explore Service
                <ArrowRight aria-hidden="true" :size="18" :stroke-width="2.2" />
              </a>
              <a class="button button--outline button--large" href="/pricing">
                View Pricing
              </a>
            </div>
            <div class="home-hero__signals" aria-label="Proxy network signals">
              <span v-for="item in homeHeroSignals" :key="item">{{ item }}</span>
            </div>
          </div>

          <aside class="home-globe-card" aria-label="Rotating global proxy network">
            <div class="home-globe-card__top">
              <span class="home-globe-card__status">
                <Globe2 aria-hidden="true" :size="16" :stroke-width="2.2" />
              </span>
              <span>Global proxy network</span>
              <strong>Live routes</strong>
            </div>

            <div class="home-globe-stage" aria-hidden="true">
              <span class="home-globe-stage__ring home-globe-stage__ring--outer"></span>
              <span class="home-globe-stage__ring home-globe-stage__ring--inner"></span>
              <span class="home-globe-stage__beam home-globe-stage__beam--one"></span>
              <span class="home-globe-stage__beam home-globe-stage__beam--two"></span>
              <HomeGlobe />
            </div>

            <div class="home-globe-card__metrics">
              <span>
                <strong>1.3M+</strong>
                <small>IP pool</small>
              </span>
              <span>
                <strong>200+</strong>
                <small>regions</small>
              </span>
              <span>
                <strong>24h</strong>
                <small>sticky</small>
              </span>
            </div>

            <div class="home-globe-card__routes">
              <a v-for="item in homeCommandLinks" :key="item.label" :href="item.href" class="home-globe-route">
                <span class="home-globe-route__icon">
                  <component :is="item.icon" aria-hidden="true" :size="18" :stroke-width="2.2" />
                </span>
                <span>
                  <strong>{{ item.label }}</strong>
                  <small>{{ item.description }}</small>
                </span>
                <ArrowUpRight aria-hidden="true" :size="16" :stroke-width="2.2" />
              </a>
            </div>
          </aside>
        </div>
      </section>

      <section class="section home-distribution-section">
        <div class="container">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--definition">Service Guide</span>
            <h2>Choose the Right Proxy Service Faster.</h2>
          </div>

          <div class="home-route-grid">
            <a
              v-for="card in homeEntryCards"
              :key="card.title"
              class="home-route-card"
              :class="`home-route-card--${card.tone}`"
              :href="card.href"
            >
              <span class="home-route-card__icon">
                <component :is="card.icon" aria-hidden="true" :size="26" :stroke-width="2.1" />
              </span>
              <h3>{{ card.title }}</h3>
              <p>{{ card.description }}</p>
              <span class="home-route-card__cta">
                {{ card.cta }}
                <ArrowRight aria-hidden="true" :size="17" :stroke-width="2.2" />
              </span>
            </a>
          </div>
        </div>
      </section>

      <section class="section home-solution-section">
        <div class="container home-solution-layout">
          <div class="home-solution-copy">
            <span class="section-label section-label--use-cases">Solution Map</span>
            <h2>Proxy Infrastructure for Data Workflows That Need Stability.</h2>
            <p>
              Bring sticky sessions, protocol setup, per-IP pricing, and routing controls together
              for scraping, monitoring, automation, and account operations.
            </p>
            <a class="home-text-link" href="/use-cases">
              Explore workflow features
              <ArrowRight aria-hidden="true" :size="17" :stroke-width="2.2" />
            </a>
          </div>

          <div class="home-solution-board" aria-label="Solution overview">
            <article v-for="item in homeSolutionCards" :key="item.title" class="home-solution-card">
              <span class="home-solution-card__line" aria-hidden="true"></span>
              <span class="home-solution-card__icon">
                <component :is="item.icon" aria-hidden="true" :size="30" :stroke-width="2.1" />
              </span>
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
              <a :href="item.href">
                {{ item.cta }}
                <ArrowUpRight aria-hidden="true" :size="16" :stroke-width="2.2" />
              </a>
            </article>
          </div>
        </div>
      </section>

      <section class="section section--alt home-use-case-section">
        <div class="container">
          <div class="section-heading">
            <span class="section-label section-label--why">Use Cases</span>
            <h2>Built for Scraping, Monitoring, Automation, and Account Operations.</h2>
            <p>
              Explore common workflows that need stable sessions, cleaner geo routing, and
              predictable proxy behavior across production tasks.
            </p>
          </div>

          <div class="use-case-grid home-use-case-grid">
            <a v-for="item in homeUseCaseCards" :key="item.title" class="use-case-card" href="/use-cases">
              <div class="use-case-card__top">
                <span class="use-case-card__icon" aria-hidden="true">
                  <component :is="item.icon" :size="32" :stroke-width="2.2" />
                </span>
              </div>
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
              <span class="use-case-card__signal">{{ item.signal }}</span>
            </a>
          </div>
        </div>
      </section>

      <section class="section section--alt home-proof-section">
        <div class="container home-proof-panel">
          <div class="home-proof-panel__copy">
            <h2>1.3M+ ISP IPs Across 200+ Countries and Regions.</h2>
            <p>
              Access authentic, stable, high-success-rate ISP proxy resources built for ad verification,
              account operations, and global business workflows.
            </p>
            <div class="home-proof-panel__signals" aria-label="Trust and rollout signals">
              <span v-for="signal in homeProofSignals" :key="signal">{{ signal }}</span>
            </div>
          </div>

          <div class="stats-row home-stats-row" aria-label="Network proof points">
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

      <section class="section home-country-section">
        <div class="container home-country-layout">
          <div class="home-country-copy">
            <span class="section-label section-label--coverage">Global Coverage</span>
            <h2>Popular Country Pools Across a 90M+ Residential IP Network.</h2>
            <p>
              Check priority markets at a glance with popular country pools drawn from an estimated
              90M+ global residential IP network.
            </p>
          </div>

          <div class="home-country-panel" aria-label="Popular country IP pool preview">
            <div class="home-country-carousel">
              <div class="home-country-track">
                <article
                  v-for="(country, index) in homeCountryCarouselPools"
                  :key="`${country.name}-${index}`"
                  :aria-hidden="index >= homeCountryPools.length ? 'true' : undefined"
                  class="home-country-card"
                >
                  <img
                    class="home-country-card__flag"
                    :src="flagIcon(country.flagCode)"
                    alt=""
                    aria-hidden="true"
                    loading="lazy"
                  />
                  <span>
                    <strong>{{ country.name }}</strong>
                    <small>{{ country.region }}</small>
                  </span>
                  <b>{{ country.ipCount }}</b>
                </article>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section section--dark quick-start-section">
        <div class="container quick-start">
          <div class="quick-start__copy">
            <span class="section-label section-label--dark section-label--quick">Quick Start</span>
            <h2>Ship Your First Scraping Request in Minutes.</h2>
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

      <section class="section home-pricing-preview-section">
        <div class="container home-pricing-preview">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--pricing">Pricing Preview</span>
            <h2>Preview Static ISP Pricing Before You Choose a Plan.</h2>
            <p>
              Compare starter, growth, premium, and enterprise options with predictable per-IP
              packages.
            </p>
          </div>

          <div class="pricing-page-plan-grid home-pricing-grid">
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
              <a
                class="button"
                :class="plan.featured ? 'button--primary' : 'button--outline'"
                href="/pricing/static-isp-proxies#pricing-page-final"
              >
                <Headphones v-if="plan.cta === 'Talk to Sales'" aria-hidden="true" :size="16" :stroke-width="2.2" />
                {{ plan.cta }}
                <ChevronRight v-if="plan.cta !== 'Talk to Sales'" aria-hidden="true" :size="17" :stroke-width="2.4" />
              </a>
            </article>
          </div>

          <div class="home-pricing-preview__actions">
            <a class="button button--primary button--large" href="/pricing/static-isp-proxies">
              View Static ISP Pricing
              <ArrowRight aria-hidden="true" :size="18" :stroke-width="2.2" />
            </a>
            <a class="button button--outline button--large" href="/faq#faq-contact">Talk to Sales</a>
          </div>
        </div>
      </section>

      <section class="section section--alt home-resource-section">
        <div class="container home-resource-layout">
          <article class="home-coverage-card">
            <h2>Explore Priority Markets and Coverage Signals.</h2>
            <p>
              Review popular markets now, with more country-level inventory details available as
              coverage expands.
            </p>
            <div class="home-market-pills" aria-label="Coverage preview markets">
              <span v-for="market in homeMarketPills" :key="market.name" class="home-market-pill">
                <img :src="flagIcon(market.flagCode)" alt="" aria-hidden="true" loading="lazy" />
                {{ market.name }}
              </span>
            </div>
          </article>

          <div class="home-resource-list" aria-label="Resource links">
            <a v-for="resource in homeResourceLinks" :key="resource.title" class="home-resource-card" :href="resource.href">
              <component :is="resource.icon" aria-hidden="true" :size="22" :stroke-width="2.2" />
              <span>
                <strong>{{ resource.title }}</strong>
                <small>{{ resource.description }}</small>
              </span>
              <ArrowUpRight aria-hidden="true" :size="17" :stroke-width="2.2" />
            </a>
          </div>
        </div>
      </section>

      <section class="final-cta">
        <div class="container final-cta__inner">
          <span class="section-label section-label--dark section-label--ready">Need Help Choosing?</span>
          <h2>Tell Us Your Workflow. We Will Recommend the Right Proxy Setup.</h2>
          <p>
            Share your target countries, session needs, traffic volume, and rollout stage. Our team
            can help map the right service, pricing, and support path.
          </p>
          <div class="final-cta__actions">
            <a class="button button--primary button--large" href="/pricing/static-isp-proxies#pricing-page-final">View Pricing</a>
            <a class="button button--dark-outline button--large" href="/faq#faq-contact">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isUseCasesPage" id="top" class="use-cases-page">
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
              <a class="button button--primary button--large" href="/pricing/static-isp-proxies#pricing-page-final">View Pricing</a>
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
                <i>ROLA-IP Gateway</i>
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
            <span class="section-label section-label--stats">Why ROLA-IP</span>
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
                    <img class="setup-tool-strip__logo" :src="curlLogo" alt="" aria-hidden="true" />
                    curl
                  </span>
                  <span>
                    <img class="setup-tool-strip__logo" :src="pythonLogo" alt="" aria-hidden="true" />
                    Python
                  </span>
                  <span>
                    <img class="setup-tool-strip__logo setup-tool-strip__logo--playwright" :src="playwrightLogo" alt="" aria-hidden="true" />
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
                    <small>gateway.rola-ip.com:9000</small>
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
              Compare proxy types by target risk, session length, budget, and trust requirements
              before you connect a production workflow.
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
            <h2>Ship Your First Scraping Request in Minutes.</h2>
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
            <h2>Proxy Workflows That Deserve Dedicated Session Design.</h2>
            <p>
              Match proxy type, market routing, and session length to the operational risk behind
              each collection job.
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
            ROLA-IP is designed for legitimate research, monitoring, and automation. Enterprise
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
              Review practical customer quotes, third-party review signals, and rollout-ready
              documentation before your team scales collection.
            </p>
            <div class="scraping-awards" aria-label="Review and media signals">
              <a
                v-for="award in scrapingAwards"
                :key="award.label"
                :href="award.href"
                :target="award.external ? '_blank' : undefined"
                :rel="award.external ? 'noopener noreferrer' : undefined"
              >
                {{ award.label }}
              </a>
            </div>
          </div>

          <div
            class="scraping-proof-window"
            @mouseenter="pauseProofCarousel"
            @mouseleave="resumeProofCarousel"
            @focusin="pauseProofCarousel"
            @focusout="resumeProofCarousel"
          >
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
                <a
                  class="scraping-proof-card__detail"
                  href="#use-case-faq"
                  :aria-label="`View details for ${quote.author}'s quote`"
                >
                  View Details
                  <ArrowUpRight aria-hidden="true" :size="16" :stroke-width="2.2" />
                </a>
              </article>
            </div>
          </div>
        </div>
      </section>

      <section id="use-case-faq" class="section faq-section use-cases-faq">
        <div class="container faq-wrap">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--faq">Frequently Asked Questions</span>
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
            <a class="button button--primary button--large" href="/pricing/static-isp-proxies#pricing-page-final">View Pricing</a>
            <a class="button button--dark-outline button--large" href="/faq#faq-contact">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isPricingIndexPage" id="top" class="pricing-index-page">
      <section class="pricing-index-hero">
        <div class="container pricing-index-hero__inner">
          <span class="section-label section-label--pricing">Pricing</span>
          <h1>Proxy Pricing for Every Data Collection Workflow.</h1>
          <p>
            Choose the proxy type that matches your traffic pattern, session needs, and rollout
            stage. Static ISP pricing is available now; the remaining proxy categories are ready for
            upcoming package details.
          </p>
        </div>
      </section>

      <section class="section pricing-index-catalog">
        <div class="container">
          <div class="pricing-product-grid">
            <component
              :is="product.available ? 'a' : 'article'"
              v-for="product in pricingProductCategories"
              :key="product.title"
              class="pricing-product-card"
              :class="{ 'pricing-product-card--available': product.available }"
              :href="product.available ? product.href : undefined"
              :aria-label="product.available ? `${product.title} pricing details` : undefined"
            >
              <span
                class="pricing-product-card__mark"
                :class="[
                  `pricing-product-card__mark--${product.tone}`,
                  `pricing-product-card__mark--${product.group}`,
                ]"
                aria-hidden="true"
              >
                <span class="pricing-product-card__glyph" v-html="product.iconSvg"></span>
              </span>
              <span class="pricing-product-card__status">{{ product.status }}</span>
              <h2>{{ product.title }}</h2>
              <p>{{ product.description }}</p>
              <div class="pricing-product-card__meta" aria-label="Pricing category details">
                <span v-for="item in product.meta" :key="item">{{ item }}</span>
              </div>
              <span class="pricing-product-card__link">
                {{ product.cta }}
                <ArrowRight aria-hidden="true" :size="17" :stroke-width="2.2" />
              </span>
            </component>
          </div>
        </div>
      </section>

      <section class="section faq-section pricing-index-faq">
        <div class="container faq-wrap">
          <div class="section-heading section-heading--center">
            <span class="section-label section-label--faq">Pricing FAQ</span>
            <h2>Choose the Right Proxy Type Before You Pick a Plan.</h2>
          </div>

          <div class="faq-list">
            <details
              v-for="(item, index) in pricingIndexFaqItems"
              :key="item.question"
              class="faq-item"
              :open="openPricingIndexFaqIndex === index"
            >
              <summary @click.prevent="openPricingIndexFaq(index)">
                <span>{{ item.question }}</span>
              </summary>
              <p>{{ item.answer }}</p>
            </details>
          </div>
        </div>
      </section>

      <section class="final-cta">
        <div class="container final-cta__inner">
          <span class="section-label section-label--dark section-label--ready">Need a Recommendation?</span>
          <h2>Tell Us the Workflow, and We Will Point You to the Right Proxy Type.</h2>
          <p>
            Start with static ISP inventory today, or talk to sales about upcoming residential,
            datacenter, dedicated, and mobile proxy packages.
          </p>
          <div class="final-cta__actions">
            <a class="button button--primary button--large" href="/pricing/static-isp-proxies">View Static ISP Pricing</a>
            <a class="button button--dark-outline button--large" href="/faq#faq-contact">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isStaticIspPricingPage" id="top" class="pricing-page">
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
              <component :is="metric.icon" aria-hidden="true" :size="24" :stroke-width="2" />
              <strong>{{ metric.value }}</strong>
              <span>{{ metric.label }}</span>
            </article>
          </div>

          <div class="pricing-table-shell">
            <div id="pricing-plans" class="pricing-page-plan-grid">
              <article
                v-for="plan in pricingPagePlans"
                :key="plan.name"
                class="pricing-page-card"
                :class="{ 'pricing-page-card--featured': plan.featured }"
                :id="plan.name === 'Enterprise' ? 'pricing-custom-terms' : undefined"
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
                  <Headphones v-if="plan.cta === 'Talk to Sales'" aria-hidden="true" :size="16" :stroke-width="2.2" />
                  {{ plan.cta }}
                  <ChevronRight v-if="plan.cta !== 'Talk to Sales'" aria-hidden="true" :size="17" :stroke-width="2.4" />
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
              Every package keeps the same core proxy controls, while inventory size and support
              depth scale with your rollout.
            </p>
          </div>
          <div class="pricing-page-include-grid">
            <article v-for="item in pricingPlanIncludes" :key="item.title" class="pricing-page-include-card">
              <CheckCircle2 aria-hidden="true" :size="20" :stroke-width="2.4" />
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
              Plan monthly cost from inventory size instead of translating every workflow into
              bandwidth estimates, minimum commitments, or unclear usage rules.
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
              <span class="pricing-page-capability-card__icon">
                <component :is="item.icon" aria-hidden="true" :size="24" :stroke-width="2" />
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
              <h2>Compliance Signals You Can Verify Before Purchase.</h2>
              <p>
                Review security documentation, privacy coverage, and sourcing standards before
                moving a plan into production.
              </p>
            </div>
            <div class="pricing-certification-strip" aria-label="Compliance and security documentation">
              <div class="compliance-icon-grid">
                <article
                  v-for="cert in complianceCertifications"
                  :key="cert.label"
                  class="compliance-icon-card"
                  :class="`compliance-icon-card--${cert.tone}`"
                  :aria-label="`${cert.label} documentation signal`"
                >
                  <img class="compliance-icon-card__image" :src="cert.image" :alt="cert.alt" loading="lazy" />
                  <span class="compliance-icon-card__label">{{ cert.label }}</span>
                  <span class="compliance-icon-card__meta">{{ cert.meta }}</span>
                </article>
              </div>
              <p class="pricing-certification-strip__copy">
                Ethically sourced IPs with security documentation, privacy terms, and procurement
                support available on request.
              </p>
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
              Review security signals, acceptable-use guidance, and procurement support before
              choosing an enterprise plan.
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
            <h2>Questions Teams Ask Before Checkout.</h2>
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
            Start with static ISP inventory for one production workflow, or talk to sales for custom
            markets, security review, and enterprise terms.
          </p>
          <div class="final-cta__actions">
            <a class="button button--primary button--large" href="#pricing">Choose Plan</a>
            <a class="button button--dark-outline button--large" href="/faq#faq-contact">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isUpcomingPricingPage && activeUpcomingPricingProduct" id="top" class="pricing-upcoming-page">
      <section class="pricing-upcoming-page__hero">
        <div class="container pricing-upcoming-page__inner">
          <div class="pricing-upcoming-page__copy">
            <span class="section-label section-label--pricing">Pricing Preview</span>
            <h1>
              {{ activeUpcomingPricingProduct.title }}
              <span>pricing is coming soon.</span>
            </h1>
            <p>
              Public packages are being prepared. Use the preview price below to plan early, or
              contact support if this product matches your current workflow.
            </p>
            <div class="pricing-upcoming-page__price">
              <span>{{ activeUpcomingPricingProduct.badge }}</span>
              <strong data-no-translate>{{ activeUpcomingPricingProduct.price }}</strong>
            </div>
            <div class="pricing-upcoming-page__actions">
              <a class="button button--primary button--large" href="/faq#faq-contact">Talk to Sales</a>
              <a class="button button--outline button--large" href="/pricing">Back to Pricing</a>
            </div>
            <div class="pricing-upcoming-page__signals" aria-label="Upcoming pricing details">
              <span>Package details</span>
              <span>Route availability</span>
              <span>Support scope</span>
            </div>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isCoveragePage" id="top" class="coverage-coming-page">
      <section class="coverage-coming-page__hero">
        <div class="container coverage-coming-page__inner">
          <div class="coverage-coming-page__copy">
            <span class="section-label section-label--coverage">Coverage</span>
            <h1>
              Coverage is
              <span>Coming Soon.</span>
            </h1>
            <p>
              Country availability, market routing, and inventory signals are coming soon.
            </p>
            <div class="coverage-coming-page__actions">
              <a class="button button--primary button--large" href="/faq#faq-contact">Talk to Sales</a>
              <a class="button button--outline button--large" href="/service">Back to Service</a>
            </div>
            <div class="coverage-coming-page__signals" aria-label="Coverage availability signals">
              <span>Country availability</span>
              <span>Market routing</span>
              <span>Inventory signals</span>
            </div>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isBlogIndexPage || (isBlogDetailPath && !activeBlogPost)" id="top" class="blog-page">
      <section class="blog-hero">
        <div class="container blog-hero__inner">
          <span class="section-label section-label--definition">Blog</span>
          <h1>ROLA-IP Blog</h1>
          <p>
            Practical guidance for teams planning proxy routing, session strategy, data collection,
            and rollout governance.
          </p>
        </div>
      </section>

      <section class="section blog-index-section">
        <div class="container">
          <a v-if="showFeaturedBlogPost" class="blog-featured-card" :href="`/blog/${featuredBlogPost.slug}`">
            <span
              class="blog-card__cover blog-card__cover--featured"
              :class="`blog-card__cover--${featuredBlogPost.tone}`"
            >
              <span>{{ featuredBlogPost.category }}</span>
            </span>
            <span class="blog-featured-card__content">
              <span class="blog-card__meta">
                <span>
                  <CalendarDays aria-hidden="true" :size="15" :stroke-width="2.2" />
                  <span data-no-translate>{{ formatBlogDate(featuredBlogPost.publishedAt) }}</span>
                </span>
                <span>
                  <Clock3 aria-hidden="true" :size="15" :stroke-width="2.2" />
                  {{ featuredBlogPost.readTime }}
                </span>
              </span>
              <strong>{{ featuredBlogPost.title }}</strong>
              <small>{{ featuredBlogPost.excerpt }}</small>
              <span class="blog-card__link">
                Read article
                <ArrowRight aria-hidden="true" :size="17" :stroke-width="2.2" />
              </span>
            </span>
          </a>

          <div class="blog-card-grid" aria-label="Latest blog articles">
            <a v-for="post in paginatedBlogPosts" :key="post.slug" class="blog-card" :href="`/blog/${post.slug}`">
              <span
                class="blog-card__cover"
                :class="`blog-card__cover--${post.tone}`"
              >
                <span>{{ post.category }}</span>
              </span>
              <span class="blog-card__body">
                <span class="blog-card__meta">
                  <span>
                    <CalendarDays aria-hidden="true" :size="15" :stroke-width="2.2" />
                    <span data-no-translate>{{ formatBlogDate(post.publishedAt) }}</span>
                  </span>
                  <span>
                    <Clock3 aria-hidden="true" :size="15" :stroke-width="2.2" />
                    {{ post.readTime }}
                  </span>
                </span>
                <strong>{{ post.title }}</strong>
                <small>{{ post.excerpt }}</small>
              </span>
            </a>
          </div>

          <nav class="blog-pagination" aria-label="Blog pagination">
            <button
              type="button"
              class="blog-pagination__button"
              :disabled="blogPage === 1"
              @click="setBlogPage(blogPage - 1)"
            >
              {{ blogPreviousLabel }}
            </button>
            <span class="blog-pagination__status">{{ blogPaginationLabel }}</span>
            <button
              type="button"
              class="blog-pagination__button"
              :disabled="blogPage === blogPageCount"
              @click="setBlogPage(blogPage + 1)"
            >
              {{ blogNextLabel }}
            </button>
          </nav>
        </div>
      </section>
    </main>

    <main v-else-if="isBlogDetailPage && activeBlogPost" id="top" class="blog-detail-page">
      <article>
        <header class="blog-detail-hero">
          <div class="container blog-detail-hero__inner">
            <a class="blog-detail__back" href="/blog">
              <ArrowRight aria-hidden="true" :size="16" :stroke-width="2.2" />
              Back to Blog
            </a>
            <h1>{{ activeBlogPost.title }}</h1>
            <p>{{ activeBlogPost.excerpt }}</p>
            <div class="blog-detail__meta">
              <span data-no-translate>{{ formatBlogDate(activeBlogPost.publishedAt) }}</span>
              <span>{{ activeBlogPost.readTime }}</span>
            </div>
          </div>
        </header>

        <div class="container">
          <div class="blog-detail__layout">
            <aside class="blog-detail__aside">
              <span>Article Guide</span>
              <a v-for="section in activeBlogPost.sections" :key="section.heading" :href="`#${slugify(section.heading)}`">
                {{ section.heading }}
              </a>
            </aside>
            <div class="blog-detail__content">
              <section v-for="section in activeBlogPost.sections" :id="slugify(section.heading)" :key="section.heading">
                <h2>{{ section.heading }}</h2>
                <p v-for="paragraph in section.paragraphs" :key="paragraph">{{ paragraph }}</p>
              </section>
            </div>
          </div>
        </div>
      </article>
    </main>

    <main v-else-if="isFaqPage" id="top" class="faq-page">
      <section class="faq-page-hero">
        <div class="container faq-page-hero__inner">
          <div class="faq-page-hero__copy">
            <span class="section-label section-label--faq">Frequently Asked Questions</span>
            <h1>Answers Before You Build with <span class="faq-page-hero__brand">ROLA-IP.</span></h1>
            <p>
              Search practical answers about pricing, routing, sessions, compliance review,
              product setup, and rollout support before you choose a plan.
            </p>
          </div>

          <div class="faq-page-search" role="search">
            <Search aria-hidden="true" :size="20" :stroke-width="2" />
            <input
              v-model="faqPageSearch"
              aria-label="Search frequently asked questions"
              type="search"
              placeholder="Search frequently asked questions..."
              @input="openFaqPageIndex = 0"
            />
          </div>
        </div>
      </section>

      <section class="section faq-page-body">
        <div class="container faq-page-layout">
          <div class="faq-page-results">
            <div v-if="visibleFaqPageItems.length" class="faq-list faq-page-list">
              <details
                v-for="(item, index) in visibleFaqPageItems"
                :key="item.id"
                class="faq-item"
                :open="openFaqPageIndex === index"
              >
                <summary @click.prevent="openFaqPage(index)">
                  <span>{{ item.question }}</span>
                </summary>
                <p>{{ item.answer }}</p>
              </details>
            </div>

            <div v-else class="faq-page-empty">
              <Search aria-hidden="true" :size="22" :stroke-width="2" />
              <h3>No matching questions yet.</h3>
              <p>Try a broader keyword, or clear filters to see the full FAQ set.</p>
            </div>
          </div>
        </div>
      </section>

      <section id="faq-contact" class="section faq-page-contact">
        <div class="container faq-page-contact__inner">
          <div class="faq-page-contact__copy">
            <h2>Still Have Questions? We Can Help.</h2>
            <p>
              Send us your endpoint setup, routing target, session pattern, or rollout issue. We
              will help you check the technical details before you move forward.
            </p>
          </div>
          <div class="faq-page-contact__actions">
            <a class="button button--primary button--large" href="mailto:support@rola-ip.com">
              <Headphones aria-hidden="true" :size="18" :stroke-width="2.2" />
              <span>Contact Support</span>
            </a>
            <a class="button button--outline button--large" href="/pricing/static-isp-proxies#pricing-page-final">
              <span>View Pricing</span>
              <ArrowRight aria-hidden="true" :size="18" :stroke-width="2.2" />
            </a>
          </div>
        </div>
      </section>
    </main>

    <main v-else-if="isServicePage" id="top">
      <section class="hero">
        <StarsBackground class="hero__stars" :factor="0.075" :speed="50" star-color="#ffffff" />
        <div class="container hero__grid">
          <div class="hero__content">
            <h1>
              <span class="grad-text">ISP / Static </span>
              <br />
              <span class="grad-text">Residential Proxies</span>
            </h1>
            <p class="hero__sub">
              Stable ISP-assigned identities for teams running account operations, verification,
              research, and automation, with predictable per-IP pricing instead of messy bandwidth
              math.
            </p>

            <div class="hero__actions">
              <a class="button button--primary button--large" href="#pricing">Choose Plan</a>
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
            <h2>Transparent per-IP Plans for Teams That Need Predictable Scaling.</h2>
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
              <a
                class="button"
                :class="plan.featured ? 'button--primary' : 'button--outline'"
                :href="plan.cta === 'Talk to Sales' ? '/faq#faq-contact' : '#faq'"
              >
                <Headphones v-if="plan.cta === 'Talk to Sales'" aria-hidden="true" :size="16" :stroke-width="2.2" />
                {{ plan.cta }}
                <ChevronRight v-if="plan.cta !== 'Talk to Sales'" aria-hidden="true" :size="17" :stroke-width="2.4" />
              </a>
            </article>
          </div>
        </div>
      </section>

      <section id="coverage" class="section">
        <div class="container">
          <div class="section-heading">
            <span class="section-label section-label--coverage">Geo Coverage</span>
            <h2>Coverage Across Priority Markets for Research and Operations.</h2>
            <p>
              Check priority regions for research, verification, monitoring, and account operations
              at a glance.
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
              <img
                class="coverage-card__flag"
                :src="flagIcon(region.flagCode)"
                alt=""
                aria-hidden="true"
                loading="lazy"
              />
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
            <h2 id="network-title">Control Sessions, Routing, and Rollout Rules from One Operational Layer.</h2>
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

          <div class="use-case-grid service-use-case-grid">
            <article v-for="useCase in useCases" :key="useCase.title" class="use-case-card">
              <div class="use-case-card__top">
                <span class="use-case-card__icon" aria-hidden="true">
                  <component :is="useCase.icon" :size="32" :stroke-width="2.2" />
                </span>
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
            <h2>Ship Your First Sticky-Session Request in Minutes.</h2>
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
              <span class="section-label section-label--why section-label--why-isp">Why ISP</span>
              <h2>Why Static ISP Proxies Outperform on Session-Sensitive Workflows.</h2>
              <p>
                Compare when static ISP proxies fit better than rotating residential or datacenter
                options, especially for login-heavy and stateful use cases.
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
            <span class="section-label section-label--definition">Best Fit</span>
            <h3>Use Static ISP When the Same Workflow Needs the Same Trusted IP.</h3>
            <p>
              This card is the short answer to the table: choose Static ISP for tasks that break when
              IP identity changes too often.
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
              <h2>Security Signals You Can Verify Before Rollout.</h2>
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
                  :aria-label="`${cert.label} documentation signal`"
                >
                  <img class="compliance-icon-card__image" :src="cert.image" :alt="cert.alt" loading="lazy" />
                  <span class="compliance-icon-card__label">{{ cert.label }}</span>
                  <span class="compliance-icon-card__meta">{{ cert.meta }}</span>
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
            <span class="section-label section-label--faq">Frequently Asked Questions</span>
            <h2>Questions Teams Ask Before Rollout.</h2>
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
            <a class="button button--primary button--large" href="#pricing">Choose Plan</a>
            <a class="button button--dark-outline button--large" href="/faq#faq-contact">Talk to Sales</a>
          </div>
        </div>
      </section>
    </main>

    <div
      ref="footerDrawerRef"
      class="footer-drawer"
      :class="{ 'footer-drawer--language-open': isFooterLanguageOpen }"
    >
      <SiteFooter />
      <div class="footer-language-bar" data-no-translate>
        <button
          type="button"
          class="footer-language-bar__handle"
          :aria-expanded="isFooterLanguageOpen"
          aria-controls="footer-language-switcher"
          @click="toggleFooterLanguageDrawer"
        >
          {{ languageSwitcherLabel }}
        </button>
        <div
          id="footer-language-switcher"
          class="language-switcher site-language site-language--bottom"
          aria-label="Footer language selector"
        >
          <button
            v-for="language in languageOptions"
            :key="`footer-${language.code}`"
            type="button"
            :class="{ 'language-switcher__button--active': currentLocale === language.code }"
            :aria-pressed="currentLocale === language.code"
            @click="setLocale(language.code)"
          >
            <img class="language-switcher__flag" :src="flagIcon(language.flagCode)" alt="" aria-hidden="true" />
            {{ language.nativeLabel }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, onMounted, onUnmounted, ref, watch } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import {
  ArrowRight,
  ArrowUpRight,
  BadgeCheck,
  BadgeDollarSign,
  Bot,
  CalendarDays,
  ChevronDown,
  ChevronRight,
  CheckCircle2,
  Clock3,
  Code2,
  Copy,
  Database,
  DollarSign,
  Fingerprint,
  Gamepad2,
  Globe2,
  Headphones,
  KeyRound,
  Megaphone,
  MessageCircle,
  PlugZap,
  Radio,
  Route,
  ScanSearch,
  Search,
  SearchCheck,
  ServerCog,
  Shield,
  ShieldCheck,
  ShoppingBag,
  ShoppingCart,
  Smartphone,
  TerminalSquare,
  Workflow,
  Zap,
  Share2,
  BriefcaseBusiness,
} from '@lucide/vue'
import brandLogo from './assets-rola-logo.svg'
import dynamicDatacenterIcon from './assets/service-icons/dynamic-datacenter.svg?raw'
import dynamicResidentialIcon from './assets/service-icons/dynamic-residential.svg?raw'
import ipv6Icon from './assets/service-icons/ipv6.svg?raw'
import mobileIcon from './assets/service-icons/mobile.svg?raw'
import staticDatacenterIcon from './assets/service-icons/static-datacenter.svg?raw'
import staticResidentialIcon from './assets/service-icons/static-residential.svg?raw'
import capterraLogo from './assets/brand-icons/capterra.svg'
import curlLogo from './assets/brand-icons/curl.svg'
import g2Logo from './assets/brand-icons/g2.svg'
import nodeLogo from './assets/brand-icons/nodejs.svg'
import playwrightLogo from './assets/brand-icons/playwright.svg'
import pythonLogo from './assets/brand-icons/python.svg'
import trustpilotLogo from './assets/brand-icons/trustpilot.svg'
import ccpaBadge from './assets/certifications/ccpa-mark.png'
import gdprBadge from './assets/certifications/gdpr-mark.png'
import iso27001Badge from './assets/certifications/iso-27001-mark.png'
import soc2Badge from './assets/certifications/soc-2-mark.png'
import HeroParticles from './components/HeroParticles.vue'
import HomeHeroShader from './components/HomeHeroShader.vue'
import HomeGlobe from './components/HomeGlobe.vue'
import SiteFooter from './components/SiteFooter.vue'
import StarsBackground from './components/StarsBackground.vue'
import { languageOptions, translateCopy, type Locale } from './i18n'

gsap.registerPlugin(ScrollTrigger)

const pageRoot = ref<HTMLElement | null>(null)
const storedLocale = window.localStorage.getItem('rola-locale') as Locale | null
const currentLocale = ref<Locale>(storedLocale && languageOptions.some((language) => language.code === storedLocale) ? storedLocale : 'en')
const isLanguageMenuOpen = ref(false)
const isFooterLanguageOpen = ref(false)
const footerDrawerRef = ref<HTMLElement | null>(null)
const currentLanguage = computed(() => languageOptions.find((language) => language.code === currentLocale.value) ?? languageOptions[0])
const languageSwitcherLabel = computed(() => ({
  en: 'Language',
  zh: '语言',
  ru: 'Язык',
})[currentLocale.value])
const isHeaderScrolled = ref(false)
const currentPath = ref(window.location.pathname)
const blogPage = ref(1)
const upcomingPricingPaths = [
  '/pricing/residential-proxies',
  '/pricing/datacenter-proxies',
  '/pricing/dedicated-datacenter-proxies',
  '/pricing/dedicated-isp-proxies',
  '/pricing/mobile-proxies',
  '/pricing/static-ipv6-proxies',
]
const knownPagePaths = ['/', '/service', '/use-cases', '/pricing', '/pricing/static-isp-proxies', ...upcomingPricingPaths, '/coverage', '/faq', '/blog']
const isHomePage = computed(() => currentPath.value === '/' || (!knownPagePaths.includes(currentPath.value) && !currentPath.value.startsWith('/blog/')))
const isServicePage = computed(() => currentPath.value === '/service')
const isUseCasesPage = computed(() => currentPath.value === '/use-cases')
const isPricingIndexPage = computed(() => currentPath.value === '/pricing')
const isStaticIspPricingPage = computed(() => currentPath.value === '/pricing/static-isp-proxies')
const activeUpcomingPricingProduct = computed(() => pricingMenuItems.find((item) => item.href === currentPath.value && !item.available))
const isUpcomingPricingPage = computed(() => Boolean(activeUpcomingPricingProduct.value))
const isCoveragePage = computed(() => currentPath.value === '/coverage')
const isFaqPage = computed(() => currentPath.value === '/faq')
const isBlogIndexPage = computed(() => currentPath.value === '/blog')
const isBlogDetailPath = computed(() => currentPath.value.startsWith('/blog/') && Boolean(currentPath.value.slice('/blog/'.length)))
const isBlogDetailPage = computed(() => isBlogDetailPath.value && Boolean(activeBlogPost.value))
const isLightHeaderPage = computed(() => isUseCasesPage.value || isPricingIndexPage.value || isStaticIspPricingPage.value || isUpcomingPricingPage.value || isCoveragePage.value || isFaqPage.value || isBlogIndexPage.value || isBlogDetailPage.value)
let scrollAnimationContext: ReturnType<typeof gsap.context> | undefined
let handleHeaderScroll: (() => void) | undefined
let handleLocationChange: (() => void) | undefined
let handleDocumentPointerDown: ((event: PointerEvent) => void) | undefined
let proofCarouselTimer: number | undefined
let translationObserver: MutationObserver | undefined
let isTranslatingDom = false
const textNodeSources = new WeakMap<Text, string>()
const activeScrapingTestimonialIndex = ref(0)
const shouldRunProofCarousel = ref(false)

const visibleScrapingTestimonials = computed(() => {
  return [0, 1].map((offset) => ({
    ...scrapingTestimonials[(activeScrapingTestimonialIndex.value + offset) % scrapingTestimonials.length],
    slot: offset,
  }))
})

const stopProofCarousel = () => {
  if (proofCarouselTimer) {
    window.clearInterval(proofCarouselTimer)
    proofCarouselTimer = undefined
  }
}

const startProofCarousel = () => {
  if (!shouldRunProofCarousel.value || proofCarouselTimer) {
    return
  }

  proofCarouselTimer = window.setInterval(() => {
    activeScrapingTestimonialIndex.value = (activeScrapingTestimonialIndex.value + 1) % scrapingTestimonials.length
  }, 3600)
}

const pauseProofCarousel = () => {
  stopProofCarousel()
}

const resumeProofCarousel = () => {
  startProofCarousel()
}

const normalizeCopy = (value: string) => value.replace(/\s+/g, ' ').trim()

const formatTranslatedText = (currentText: string, sourceText: string, translatedText: string) => {
  const leading = currentText.match(/^\s*/)?.[0] ?? ''
  const trailing = currentText.match(/\s*$/)?.[0] ?? ''
  const normalizedCurrent = normalizeCopy(currentText)

  if (!normalizedCurrent || translatedText === sourceText) {
    return currentText
  }

  return `${leading}${translatedText}${trailing}`
}

const shouldSkipTranslation = (element: Element | null) => {
  return Boolean(element?.closest('[data-no-translate], script, style, svg, canvas, code, pre'))
}

const translateTextNode = (node: Text) => {
  const parent = node.parentElement
  if (shouldSkipTranslation(parent)) return

  const existingSource = textNodeSources.get(node)
  const source = existingSource ?? normalizeCopy(node.textContent ?? '')
  if (!source) return

  if (!existingSource) {
    textNodeSources.set(node, source)
  }

  const translated = translateCopy(source, currentLocale.value)
  const nextText = formatTranslatedText(node.textContent ?? '', source, translated)
  if (node.textContent !== nextText) {
    node.textContent = nextText
  }
}

const translateElementAttributes = (element: Element) => {
  if (shouldSkipTranslation(element)) return

  ;(['aria-label', 'placeholder', 'title', 'alt'] as const).forEach((attribute) => {
    const currentValue = element.getAttribute(attribute)
    if (!currentValue) return

    const sourceKey = `i18nSource${attribute.replace(/[^a-z]/gi, '')}`
    const htmlElement = element as HTMLElement & Record<string, string | undefined>
    const source = htmlElement.dataset?.[sourceKey] ?? normalizeCopy(currentValue)
    if (!source) return

    if (htmlElement.dataset && !htmlElement.dataset[sourceKey]) {
      htmlElement.dataset[sourceKey] = source
    }

    const translated = translateCopy(source, currentLocale.value)
    if (translated !== currentValue) {
      element.setAttribute(attribute, translated)
    }
  })
}

const translateDomCopy = () => {
  if (!pageRoot.value || isTranslatingDom) return

  isTranslatingDom = true
  const root = pageRoot.value
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT)
  const textNodes: Text[] = []

  while (walker.nextNode()) {
    textNodes.push(walker.currentNode as Text)
  }

  textNodes.forEach(translateTextNode)
  root.querySelectorAll<HTMLElement>('[aria-label], [placeholder], [title], [alt]').forEach(translateElementAttributes)
  document.documentElement.lang = currentLocale.value === 'zh' ? 'zh-CN' : currentLocale.value
  isTranslatingDom = false
}

const setLocale = (locale: Locale) => {
  currentLocale.value = locale
  isLanguageMenuOpen.value = false
}

const toggleLanguageMenu = () => {
  isLanguageMenuOpen.value = !isLanguageMenuOpen.value
}

const closeLanguageMenu = () => {
  isLanguageMenuOpen.value = false
}

const toggleFooterLanguageDrawer = async () => {
  isFooterLanguageOpen.value = !isFooterLanguageOpen.value

  if (isFooterLanguageOpen.value) {
    await nextTick()
    footerDrawerRef.value?.scrollIntoView({ block: 'end', behavior: 'smooth' })
  }
}

const closeLanguageMenuOnOutsideClick = (event: PointerEvent) => {
  if (!isLanguageMenuOpen.value) return

  const target = event.target
  if (target instanceof Element && target.closest('[data-language-select]')) {
    return
  }

  closeLanguageMenu()
}

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
    if (currentPath.value !== '/blog') {
      blogPage.value = 1
    }
    nextTick(translateDomCopy)
  }
  handleLocationChange()
  window.addEventListener('hashchange', handleLocationChange)
  window.addEventListener('popstate', handleLocationChange)

  handleDocumentPointerDown = closeLanguageMenuOnOutsideClick
  document.addEventListener('pointerdown', handleDocumentPointerDown)

  handleHeaderScroll = () => {
    isHeaderScrolled.value = window.scrollY > 16
  }
  handleHeaderScroll()
  window.addEventListener('scroll', handleHeaderScroll, { passive: true })

  translationObserver = new MutationObserver(() => {
    if (!isTranslatingDom) {
      window.requestAnimationFrame(translateDomCopy)
    }
  })
  if (pageRoot.value) {
    translationObserver.observe(pageRoot.value, {
      attributes: true,
      attributeFilter: ['aria-label', 'placeholder', 'title', 'alt'],
      childList: true,
      subtree: true,
    })
  }
  translateDomCopy()

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  shouldRunProofCarousel.value = isUseCasesPage.value && !prefersReducedMotion
  startProofCarousel()

  if (!pageRoot.value || prefersReducedMotion) {
    return
  }

  scrollAnimationContext = gsap.context(() => {
    const animatedSelectors = [
      '.hero-demo',
      '.home-route-card',
      '.home-solution-card',
      '.home-country-card',
      '.home-resource-card',
      '.stat-card',
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
      '.blog-featured-card',
      '.blog-card',
      '.blog-detail__content section',
      '.faq-item',
    ]
    const animatedElements = animatedSelectors.flatMap((selector) =>
      Array.from(document.querySelectorAll<HTMLElement>(selector)),
    )
    const belowInitialViewport = (element: HTMLElement) => element.getBoundingClientRect().top > window.innerHeight

    gsap.set(animatedElements, { willChange: 'transform, opacity' })

    gsap.utils
      .toArray<HTMLElement>(
        '.home-route-card, .home-solution-card, .home-country-card, .home-resource-card, .stat-card, .performance-layout, .pricing-card, .coverage-card, .network-card, .quick-start-card, .feature-card, .testimonial-card, .compliance-panel, .scraping-challenge-card, .scraping-capability-card, .proxy-type-card, .use-cases-page-card, .scraping-compliance-panel, .blog-featured-card, .blog-card, .blog-detail__content section, .faq-item',
      )
      .filter(belowInitialViewport)
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
  if (handleDocumentPointerDown) {
    document.removeEventListener('pointerdown', handleDocumentPointerDown)
  }
  scrollAnimationContext?.revert()
  stopProofCarousel()
  translationObserver?.disconnect()
})

watch(currentLocale, (locale) => {
  window.localStorage.setItem('rola-locale', locale)
  nextTick(translateDomCopy)
})

const navItems = [
  { label: 'Proxies', href: '/service', dropdown: 'service' },
  { label: 'Features', href: '/use-cases' },
  { label: 'Pricing', href: '/pricing', dropdown: 'pricing' },
  { label: 'Purposes', href: '/use-cases', dropdown: 'purposes' },
  { label: 'Blog', href: '/blog' },
  { label: 'FAQ', href: '/faq' },
]

const serviceMenuItems = [
  {
    title: 'Dynamic Residential IP',
    description: 'Real-user residential pools for anonymous data collection.',
    href: '/service',
    iconSvg: dynamicResidentialIcon,
    tone: 'purple',
    group: 'dynamic',
  },
  {
    title: 'Static Residential IP',
    description: 'Sticky residential identity for stable account workflows.',
    href: '/service',
    iconSvg: staticResidentialIcon,
    tone: 'blue',
    group: 'static',
  },
  {
    title: 'Dynamic Datacenter IP',
    description: 'Fast rotating proxy access for scale and monitoring.',
    href: '/service',
    iconSvg: dynamicDatacenterIcon,
    tone: 'sky',
    group: 'dynamic',
  },
  {
    title: 'Static Datacenter IP',
    description: 'Dedicated static routes for predictable high-volume jobs.',
    href: '/service',
    iconSvg: staticDatacenterIcon,
    tone: 'amber',
    group: 'static',
  },
  {
    title: 'Mobile IP',
    description: 'Mobile network profiles for app and device simulation.',
    href: '/service',
    iconSvg: mobileIcon,
    tone: 'mint',
    group: 'dynamic',
  },
  {
    title: 'Static IPv6',
    description: 'Long-lived IPv6 proxy access for stable collection flows.',
    href: '/service',
    iconSvg: ipv6Icon,
    tone: 'green',
    group: 'static',
  },
]

const pricingMenuItems = [
  {
    title: 'Dynamic Residential IP',
    description: 'Rotating residential pools for broad public data collection.',
    badge: 'Most popular',
    price: '$1.08/GB',
    href: '/pricing/residential-proxies',
    iconSvg: dynamicResidentialIcon,
    tone: 'purple',
    group: 'dynamic',
    available: false,
  },
  {
    title: 'Static Residential IP',
    description: 'Sticky residential identity for stable account workflows.',
    badge: 'Dedicated ISP',
    price: '$1.30/IP',
    href: '/pricing/static-isp-proxies',
    iconSvg: staticResidentialIcon,
    tone: 'blue',
    group: 'static',
    available: true,
  },
  {
    title: 'Dynamic Datacenter IP',
    description: 'Fast rotating proxy access for scale and monitoring.',
    badge: 'Cost efficient',
    price: '$0.40/GB',
    href: '/pricing/datacenter-proxies',
    iconSvg: dynamicDatacenterIcon,
    tone: 'sky',
    group: 'dynamic',
    available: false,
  },
  {
    title: 'Static Datacenter IP',
    description: 'Dedicated static routes for predictable high-volume jobs.',
    badge: 'Dedicated datacenter',
    price: '$1.60/IP',
    href: '/pricing/dedicated-datacenter-proxies',
    iconSvg: staticDatacenterIcon,
    tone: 'amber',
    group: 'static',
    available: false,
  },
  {
    title: 'Mobile IP',
    description: 'Mobile network profiles for app and device simulation.',
    badge: 'Native carrier',
    price: '$3.20/GB',
    href: '/pricing/mobile-proxies',
    iconSvg: mobileIcon,
    tone: 'mint',
    group: 'dynamic',
    available: false,
  },
  {
    title: 'Static IPv6',
    description: 'Long-lived IPv6 proxy access for stable collection flows.',
    badge: 'Dedicated IPv6',
    price: '$0.80/IP',
    href: '/pricing/static-ipv6-proxies',
    iconSvg: ipv6Icon,
    tone: 'green',
    group: 'static',
    available: false,
  },
]

const purposeHref = '/use-cases'
const platformIcon = (domain: string) => `https://www.google.com/s2/favicons?domain=${domain}&sz=64`

const purposeMenuSections = [
  {
    title: 'E-commerce',
    icon: ShoppingCart,
    href: purposeHref,
    platforms: [
      { name: 'Amazon', icon: platformIcon('amazon.com'), href: purposeHref },
      { name: 'BestBuy', icon: platformIcon('bestbuy.com'), href: purposeHref },
      { name: 'Ebay', icon: platformIcon('ebay.com'), href: purposeHref },
      { name: 'Etsy', icon: platformIcon('etsy.com'), href: purposeHref },
      { name: 'Shopee', icon: platformIcon('shopee.com'), href: purposeHref },
      { name: 'Vinted', icon: platformIcon('vinted.com'), href: purposeHref },
    ],
  },
  {
    title: 'Social Networks',
    icon: Share2,
    href: purposeHref,
    platforms: [
      { name: 'Dating', icon: platformIcon('tinder.com'), href: purposeHref },
      { name: 'Facebook', icon: platformIcon('facebook.com'), href: purposeHref },
      { name: 'Instagram', icon: platformIcon('instagram.com'), href: purposeHref },
      { name: 'OnlyFans', icon: platformIcon('onlyfans.com'), href: purposeHref },
      { name: 'Reddit', icon: platformIcon('reddit.com'), href: purposeHref },
      { name: 'TikTok', icon: platformIcon('tiktok.com'), href: purposeHref },
      { name: '(X) Twitter', icon: platformIcon('x.com'), href: purposeHref },
    ],
  },
  {
    title: 'Games',
    icon: Gamepad2,
    href: purposeHref,
    platforms: [
      { name: 'Aion', icon: platformIcon('aiononline.com'), href: purposeHref },
      { name: 'Diablo 2', icon: platformIcon('diablo2.blizzard.com'), href: purposeHref },
      { name: 'Growtopia', icon: platformIcon('growtopiagame.com'), href: purposeHref },
      { name: 'Lords Mobile', icon: platformIcon('lordsmobile.igg.com'), href: purposeHref },
      { name: 'Minecraft', icon: platformIcon('minecraft.net'), href: purposeHref },
      { name: 'Path of Exile', icon: platformIcon('pathofexile.com'), href: purposeHref },
      { name: 'RuneScape', icon: platformIcon('runescape.com'), href: purposeHref },
      { name: 'SilkRoad', icon: platformIcon('silkroadonline.net'), href: purposeHref },
      { name: 'World of Warcraft', icon: platformIcon('worldofwarcraft.blizzard.com'), href: purposeHref },
    ],
  },
  {
    title: 'Search Engines',
    icon: Search,
    href: purposeHref,
    platforms: [
      { name: 'Bing', icon: platformIcon('bing.com'), href: purposeHref },
      { name: 'DuckDuckGo', icon: platformIcon('duckduckgo.com'), href: purposeHref },
      { name: 'Google', icon: platformIcon('google.com'), href: purposeHref },
    ],
  },
  {
    title: 'Streaming',
    icon: Radio,
    href: purposeHref,
    platforms: [
      { name: 'Spotify', icon: platformIcon('spotify.com'), href: purposeHref },
      { name: 'Twitch', icon: platformIcon('twitch.tv'), href: purposeHref },
      { name: 'Youtube', icon: platformIcon('youtube.com'), href: purposeHref },
    ],
  },
  {
    title: 'AI & Chat',
    icon: MessageCircle,
    href: purposeHref,
    paired: true,
    platforms: [
      { name: 'ChatGPT', icon: platformIcon('chatgpt.com'), href: purposeHref },
      { name: 'Discord', icon: platformIcon('discord.com'), href: purposeHref },
      { name: 'WhatsApp', icon: platformIcon('whatsapp.com'), href: purposeHref },
      { name: 'Telegram', icon: platformIcon('telegram.org'), href: purposeHref },
    ],
  },
  {
    title: 'Marketplaces',
    icon: BriefcaseBusiness,
    href: purposeHref,
    paired: true,
    platforms: [
      { name: 'Tickets', icon: platformIcon('stubhub.com'), href: purposeHref },
      { name: 'Ticketmaster', icon: platformIcon('ticketmaster.com'), href: purposeHref },
      { name: 'Upwork', icon: platformIcon('upwork.com'), href: purposeHref },
      { name: 'Sneakers', icon: platformIcon('stockx.com'), href: purposeHref },
      { name: 'Nike', icon: platformIcon('nike.com'), href: purposeHref },
      { name: 'Wikipedia', icon: platformIcon('wikipedia.org'), href: purposeHref },
      { name: 'Steam', icon: platformIcon('steampowered.com'), href: purposeHref },
      { name: 'Apple', icon: platformIcon('apple.com'), href: purposeHref },
    ],
  },
]

const purposeMenuColumns = [
  [purposeMenuSections[0], purposeMenuSections[3]],
  [purposeMenuSections[1], purposeMenuSections[4]],
  [purposeMenuSections[2], purposeMenuSections[5], purposeMenuSections[6]],
]

const blogPosts = [
  {
    slug: 'static-isp-proxy-rollout-checklist',
    category: 'Operations',
    title: 'Static ISP Proxy Rollout Checklist for Production Teams',
    excerpt:
      'Plan routing, session rules, monitoring, and procurement checkpoints before moving a static ISP proxy workflow into production.',
    publishedAt: 'June 18, 2026',
    readTime: '7 min read',
    tone: 'green',
    coverImage: '/blog-covers/static-isp-proxy-rollout-checklist.png',
    featured: true,
    sections: [
      {
        heading: 'Start with the workflow, not the proxy type',
        paragraphs: [
          'A static ISP rollout works best when the team starts from the job it needs to protect: account operations, price monitoring, ad verification, research, or another workflow where identity continuity matters.',
          'Map the target markets, session length, expected request volume, and acceptable retry budget before choosing allocation size. This keeps the proxy plan tied to operational risk instead of a generic inventory number.',
        ],
      },
      {
        heading: 'Define routing and session rules early',
        paragraphs: [
          'Country routing, sticky-session keys, endpoint naming, and fallback behavior should be documented before the first production run. The clearer these rules are, the easier it becomes to debug data quality later.',
          'Teams usually benefit from starting with one market and one session pattern, then expanding once the first route is stable.',
        ],
      },
      {
        heading: 'Measure quality before scaling',
        paragraphs: [
          'Track clean reads, challenge rate, latency, session drift, and target-level errors. These signals show whether the workflow is ready for more IPs, more markets, or a different routing strategy.',
          'A small validation window is cheaper than scaling a noisy setup. Treat the first run as an operational review, not only a technical connection test.',
        ],
      },
    ],
  },
  {
    slug: 'sticky-sessions-data-collection',
    category: 'Session Strategy',
    title: 'When Sticky Sessions Improve Data Collection Quality',
    excerpt:
      'Learn where persistent identity helps reduce noisy reads, mid-flow failures, and unnecessary retries across longer collection tasks.',
    publishedAt: 'June 12, 2026',
    readTime: '5 min read',
    tone: 'blue',
    coverImage: '/blog-covers/sticky-sessions-data-collection.png',
    featured: false,
    sections: [
      {
        heading: 'Continuity protects context',
        paragraphs: [
          'Some workflows fail when identity rotates too soon. Logged-in checks, carts, regional account states, and multi-step verification paths often need the same route long enough to complete the job.',
          'Sticky sessions help the target see a consistent context, which can reduce false changes and noisy comparisons.',
        ],
      },
      {
        heading: 'Rotation still has a place',
        paragraphs: [
          'Broad public collection may work better with rotation when each request can safely stand alone. The right choice depends on target risk, session depth, and whether downstream data depends on continuity.',
        ],
      },
    ],
  },
  {
    slug: 'proxy-cost-planning-per-ip',
    category: 'Pricing',
    title: 'How to Plan Proxy Cost with Per-IP Packages',
    excerpt:
      'A practical way to forecast proxy budget by inventory size, rollout stage, support depth, and market coverage needs.',
    publishedAt: 'June 5, 2026',
    readTime: '6 min read',
    tone: 'cyan',
    coverImage: '/blog-covers/proxy-cost-planning-per-ip.png',
    featured: false,
    sections: [
      {
        heading: 'Inventory size is the baseline',
        paragraphs: [
          'Per-IP pricing is easier to forecast when the main requirement is stable capacity. Start with the number of concurrent identities a workflow needs, then add room for market expansion and validation runs.',
        ],
      },
      {
        heading: 'Support depth changes the plan',
        paragraphs: [
          'Teams moving into production often need more than raw IPs. Onboarding, routing review, procurement documents, and support expectations can change which package is the better fit.',
        ],
      },
    ],
  },
  {
    slug: 'regional-market-monitoring-proxy-routing',
    category: 'Market Coverage',
    title: 'Proxy Routing Tips for Regional Market Monitoring',
    excerpt:
      'Use country routing, stable identity, and rollout checks to keep pricing, inventory, and search data aligned to the right market.',
    publishedAt: 'May 29, 2026',
    readTime: '4 min read',
    tone: 'purple',
    coverImage: '/blog-covers/regional-market-monitoring-proxy-routing.png',
    featured: false,
    sections: [
      {
        heading: 'Keep market context consistent',
        paragraphs: [
          'Regional monitoring becomes noisy when location context changes between requests. Country routing and stable sessions help keep price, catalog, search, and availability checks aligned to the same market.',
        ],
      },
      {
        heading: 'Review markets before expanding',
        paragraphs: [
          'Start with priority countries, review success and latency, then expand coverage. This makes the rollout easier to explain to stakeholders and easier to debug for operators.',
        ],
      },
    ],
  },
  {
    slug: 'account-operations-stable-proxy-identity',
    category: 'Account Operations',
    title: 'Stable Proxy Identity for Account Operations',
    excerpt:
      'How stable IP allocation, session review, and market routing help teams reduce account friction during repeated operational checks.',
    publishedAt: 'May 22, 2026',
    readTime: '6 min read',
    tone: 'green',
    coverImage: '/blog-covers/account-operations-stable-proxy-identity.png',
    featured: false,
    sections: [
      {
        heading: 'Keep identity predictable',
        paragraphs: [
          'Account workflows often depend on repeatable context. When the route changes too often, teams can see unnecessary verification prompts, location drift, or inconsistent account state.',
          'Stable proxy identity gives operators a clearer baseline for repeated checks, especially when the same accounts need to access the same markets over time.',
        ],
      },
      {
        heading: 'Separate markets and workflows',
        paragraphs: [
          'Use clear route labels for each market and workflow so support, engineering, and operations teams can debug problems without guessing which proxy pool was involved.',
        ],
      },
    ],
  },
  {
    slug: 'ad-verification-geo-consistency',
    category: 'Ad Verification',
    title: 'Why Geo Consistency Matters in Ad Verification',
    excerpt:
      'Use consistent country routing and review windows to keep ad placement checks aligned with the audience location being tested.',
    publishedAt: 'May 15, 2026',
    readTime: '5 min read',
    tone: 'blue',
    coverImage: '/blog-covers/ad-verification-geo-consistency.png',
    featured: false,
    sections: [
      {
        heading: 'Geo drift creates false signals',
        paragraphs: [
          'Ad verification results are easiest to trust when market context stays stable. If a request drifts between regions, placement, language, and price signals can look wrong even when the campaign is healthy.',
        ],
      },
      {
        heading: 'Validate before expanding',
        paragraphs: [
          'Start with a small set of priority countries, confirm that the target sees the intended location, then scale the check across more inventory.',
        ],
      },
    ],
  },
  {
    slug: 'scraping-monitoring-signals',
    category: 'Monitoring',
    title: 'Monitoring Signals Every Scraping Workflow Should Track',
    excerpt:
      'A short list of success, latency, retry, and challenge signals that help teams catch proxy and target issues earlier.',
    publishedAt: 'May 8, 2026',
    readTime: '7 min read',
    tone: 'cyan',
    coverImage: '/blog-covers/scraping-monitoring-signals.png',
    featured: false,
    sections: [
      {
        heading: 'Track the path, not only the result',
        paragraphs: [
          'A successful response can still hide growing risk. Teams should review latency, retry count, challenge frequency, and target-level error patterns before a workflow becomes unstable.',
        ],
      },
      {
        heading: 'Compare by market and route',
        paragraphs: [
          'Segment metrics by country, endpoint, and workflow. This makes it easier to find whether a problem is target-specific, market-specific, or related to a route configuration.',
        ],
      },
    ],
  },
  {
    slug: 'proxy-pool-sizing-production',
    category: 'Capacity Planning',
    title: 'How to Size a Proxy Pool for Production Traffic',
    excerpt:
      'Estimate IP needs with concurrency, session length, market count, and validation overhead before moving from test traffic to production.',
    publishedAt: 'May 1, 2026',
    readTime: '6 min read',
    tone: 'purple',
    coverImage: '/blog-covers/proxy-pool-sizing-production.png',
    featured: false,
    sections: [
      {
        heading: 'Start with concurrency',
        paragraphs: [
          'Pool size should follow the number of identities a workflow needs at the same time. Add room for validation, failover, and market expansion instead of sizing only around average traffic.',
        ],
      },
      {
        heading: 'Review before the next jump',
        paragraphs: [
          'Before increasing traffic, review error rate, target feedback, and support needs. A measured expansion is easier to control than a sudden large rollout.',
        ],
      },
    ],
  },
  {
    slug: 'marketplace-data-quality-proxies',
    category: 'Data Quality',
    title: 'Improving Marketplace Data Quality with Stable Routes',
    excerpt:
      'Keep marketplace price, seller, and availability checks cleaner by aligning identity, region, and collection cadence.',
    publishedAt: 'April 24, 2026',
    readTime: '5 min read',
    tone: 'green',
    coverImage: '/blog-covers/marketplace-data-quality-proxies.png',
    featured: false,
    sections: [
      {
        heading: 'Route consistency reduces noise',
        paragraphs: [
          'Marketplace pages often vary by country, account state, delivery location, and session context. Stable routing helps teams separate real market changes from collection noise.',
        ],
      },
      {
        heading: 'Cadence matters',
        paragraphs: [
          'A predictable collection schedule makes it easier to compare price, stock, and seller changes over time without overloading the workflow.',
        ],
      },
    ],
  },
  {
    slug: 'proxy-onboarding-checklist',
    category: 'Onboarding',
    title: 'Proxy Onboarding Checklist for New Data Teams',
    excerpt:
      'A practical onboarding path for credentials, endpoints, route naming, test markets, and support expectations.',
    publishedAt: 'April 17, 2026',
    readTime: '4 min read',
    tone: 'blue',
    coverImage: '/blog-covers/proxy-onboarding-checklist.png',
    featured: false,
    sections: [
      {
        heading: 'Document the basics first',
        paragraphs: [
          'New teams should know which endpoints to use, how routes are named, who owns credentials, and which market to test first. Clear setup notes reduce repeated support questions.',
        ],
      },
      {
        heading: 'Run one workflow end to end',
        paragraphs: [
          'Before adding more targets, connect one workflow, review the output, and confirm the support path. This makes later expansion more predictable.',
        ],
      },
    ],
  },
  {
    slug: 'session-rotation-vs-sticky-routing',
    category: 'Session Strategy',
    title: 'Session Rotation vs. Sticky Routing: How to Choose',
    excerpt:
      'Compare rotating and sticky sessions by target risk, task depth, identity continuity, and cost control.',
    publishedAt: 'April 10, 2026',
    readTime: '7 min read',
    tone: 'cyan',
    coverImage: '/blog-covers/session-rotation-vs-sticky-routing.png',
    featured: false,
    sections: [
      {
        heading: 'Match sessions to task depth',
        paragraphs: [
          'Short, independent requests may benefit from rotation. Multi-step workflows, account checks, and continuity-sensitive targets usually need a route that stays stable longer.',
        ],
      },
      {
        heading: 'Use both when the workflow needs both',
        paragraphs: [
          'Some teams run rotation for discovery and sticky routing for follow-up checks. Separating those stages can improve quality without overusing stable identities.',
        ],
      },
    ],
  },
  {
    slug: 'global-coverage-rollout-plan',
    category: 'Global Coverage',
    title: 'Planning a Global Coverage Rollout Without Losing Control',
    excerpt:
      'Expand proxy coverage market by market with validation checkpoints, inventory notes, and route-level reporting.',
    publishedAt: 'April 3, 2026',
    readTime: '6 min read',
    tone: 'purple',
    coverImage: '/blog-covers/global-coverage-rollout-plan.png',
    featured: false,
    sections: [
      {
        heading: 'Prioritize markets by business value',
        paragraphs: [
          'A global rollout is easier to manage when markets are grouped by priority. Start with the countries that matter most to the workflow, then add coverage after each checkpoint is stable.',
        ],
      },
      {
        heading: 'Keep route reporting simple',
        paragraphs: [
          'Operators need to know which market, endpoint, and session pattern produced each result. Route-level reporting makes support and quality review much faster.',
        ],
      },
    ],
  },
]

const featuredBlogPost = computed(() => blogPosts.find((post) => post.featured) ?? blogPosts[0])
const secondaryBlogPosts = computed(() => blogPosts.filter((post) => post.slug !== featuredBlogPost.value.slug))
const blogPostsPerPage = 10
const blogPageCount = computed(() => Math.max(1, Math.ceil(blogPosts.length / blogPostsPerPage)))
const showFeaturedBlogPost = computed(() => blogPage.value === 1)
const paginatedBlogPosts = computed(() => {
  if (showFeaturedBlogPost.value) {
    return secondaryBlogPosts.value.slice(0, blogPostsPerPage - 1)
  }

  const start = (blogPage.value - 1) * blogPostsPerPage - 1
  return secondaryBlogPosts.value.slice(start, start + blogPostsPerPage)
})
const formatBlogDate = (publishedAt: string) => {
  if (currentLocale.value === 'en') return publishedAt

  const date = new Date(`${publishedAt} 00:00:00`)
  if (Number.isNaN(date.getTime())) return publishedAt

  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')

  return `${year}.${month}.${day}`
}
const blogPreviousLabel = computed(() => ({
  en: 'Previous',
  zh: '上一页',
  ru: 'Назад',
})[currentLocale.value])
const blogNextLabel = computed(() => ({
  en: 'Next',
  zh: '下一页',
  ru: 'Вперед',
})[currentLocale.value])
const blogPaginationLabel = computed(() => ({
  en: `Page ${blogPage.value} of ${blogPageCount.value}`,
  zh: `第 ${blogPage.value} / ${blogPageCount.value} 页`,
  ru: `Страница ${blogPage.value} из ${blogPageCount.value}`,
})[currentLocale.value])
const setBlogPage = (page: number) => {
  blogPage.value = Math.min(Math.max(page, 1), blogPageCount.value)
  nextTick(translateDomCopy)
  window.requestAnimationFrame(() => {
    document.querySelector('.blog-index-section')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  })
}
const activeBlogPost = computed(() => blogPosts.find((post) => `/blog/${post.slug}` === currentPath.value))
const slugify = (value: string) =>
  value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '')

const homeHeroSignals = [
  'Static ISP identity',
  'Sticky session control',
  'Per-IP pricing',
]

const homeCommandLinks = [
  {
    label: 'Service',
    description: 'Static ISP proxy details and quick start.',
    href: '/service',
    icon: ShieldCheck,
  },
  {
    label: 'Pricing',
    description: 'Compare per-IP plans and packages.',
    href: '/pricing',
    icon: DollarSign,
  },
  {
    label: 'Features',
    description: 'See use cases for scraping and data teams.',
    href: '/use-cases',
    icon: ScanSearch,
  },
]

const homeEntryCards = [
  {
    kicker: 'Proxy Service',
    title: 'Static ISP Proxy Service',
    description:
      'Review sticky sessions, protocols, routing controls, proof points, and setup details.',
    cta: 'Open Service',
    href: '/service',
    icon: ServerCog,
    tone: 'service',
  },
  {
    kicker: 'Workflows',
    title: 'Use Cases for Data Teams',
    description:
      'Explore scraping, monitoring, account operations, and automation workflows that need stable proxy identity.',
    cta: 'View Features',
    href: '/use-cases',
    icon: Route,
    tone: 'features',
  },
  {
    kicker: 'Pricing',
    title: 'Pricing and Packages',
    description:
      'Compare 10 IP, 100 IP, 500 IP, and enterprise packages with predictable per-IP pricing.',
    cta: 'Check Pricing',
    href: '/pricing',
    icon: DollarSign,
    tone: 'pricing',
  },
  {
    kicker: 'Coverage',
    title: 'Coverage Status',
    description:
      'Check current market coverage and availability signals before planning regional rollout.',
    cta: 'View Coverage',
    href: '/coverage',
    icon: Globe2,
    tone: 'coverage',
  },
  {
    kicker: 'Support',
    title: 'FAQ and Technical Help',
    description:
      'Find answers for setup, billing, compliance, rollout planning, and support contact options.',
    cta: 'Read FAQ',
    href: '/faq',
    icon: Headphones,
    tone: 'support',
  },
]

const homeSolutionCards = [
  {
    kicker: 'Service',
    title: 'Static ISP Proxy Infrastructure',
    description:
      'Use static ISP routes for sticky sessions, protocol setup, proof points, and routing control.',
    cta: 'View Service',
    href: '/service',
    icon: Fingerprint,
    meta: 'Service details',
  },
  {
    kicker: 'Workflow',
    title: 'Data Collection and Automation Paths',
    description:
      'Match scraping, monitoring, account operation, and research workflows with the right proxy setup.',
    cta: 'View Features',
    href: '/use-cases',
    icon: Workflow,
    meta: 'Workflow paths',
  },
  {
    kicker: 'Rollout',
    title: 'Pricing, Coverage, and Support',
    description:
      'Review pricing, availability, and support options before scaling a production workflow.',
    cta: 'Compare Plans',
    href: '/pricing',
    icon: BadgeDollarSign,
    meta: 'Pricing signals',
  },
]

const homeProofSignals = [
  '99.9% success rate',
  'Transparent pricing',
  'Instant delivery',
]

const homeCountryPools = [
  { flagCode: 'US', name: 'United States', region: 'North America', ipCount: '18.6M+' },
  { flagCode: 'IN', name: 'India', region: 'Asia Pacific', ipCount: '11.4M+' },
  { flagCode: 'BR', name: 'Brazil', region: 'Latin America', ipCount: '8.7M+' },
  { flagCode: 'DE', name: 'Germany', region: 'Europe', ipCount: '6.8M+' },
  { flagCode: 'GB', name: 'United Kingdom', region: 'Europe', ipCount: '6.4M+' },
  { flagCode: 'FR', name: 'France', region: 'Europe', ipCount: '5.7M+' },
  { flagCode: 'ID', name: 'Indonesia', region: 'Asia Pacific', ipCount: '5.2M+' },
  { flagCode: 'CA', name: 'Canada', region: 'North America', ipCount: '4.9M+' },
  { flagCode: 'JP', name: 'Japan', region: 'Asia Pacific', ipCount: '4.6M+' },
  { flagCode: 'MX', name: 'Mexico', region: 'Latin America', ipCount: '4.3M+' },
  { flagCode: 'AU', name: 'Australia', region: 'Oceania', ipCount: '3.7M+' },
  { flagCode: 'ES', name: 'Spain', region: 'Europe', ipCount: '3.2M+' },
  { flagCode: 'IT', name: 'Italy', region: 'Europe', ipCount: '3.1M+' },
  { flagCode: 'NL', name: 'Netherlands', region: 'Europe', ipCount: '2.8M+' },
  { flagCode: 'SG', name: 'Singapore', region: 'Asia Pacific', ipCount: '1.7M+' },
]

const homeCountryCarouselPools = computed(() => [...homeCountryPools, ...homeCountryPools])

const homeUseCaseCards = [
  {
    icon: Bot,
    title: 'Web Scraping',
    description: 'Collect public web data with cleaner sessions and fewer avoidable retries.',
    signal: 'Data collection',
  },
  {
    icon: ShoppingBag,
    title: 'Ecommerce Monitoring',
    description: 'Track pricing, catalogs, storefront changes, and regional inventory signals.',
    signal: 'Market intelligence',
  },
  {
    icon: SearchCheck,
    title: 'SEO and SERP Checks',
    description: 'Review rankings, ads, and search results from consistent market locations.',
    signal: 'Localized visibility',
  },
  {
    icon: ShieldCheck,
    title: 'Account Operations',
    description: 'Support workflows that need identity continuity across longer session paths.',
    signal: 'Sticky identity',
  },
  {
    icon: Megaphone,
    title: 'Ad Verification',
    description: 'Check campaign delivery, landing pages, and creative behavior by geography.',
    signal: 'Geo validation',
  },
  {
    icon: Database,
    title: 'AI Data Pipelines',
    description: 'Feed collection jobs that need predictable routing and production visibility.',
    signal: 'Reliable inputs',
  },
]

const homeMarketPills = [
  { flagCode: 'US', name: 'United States' },
  { flagCode: 'GB', name: 'United Kingdom' },
  { flagCode: 'DE', name: 'Germany' },
  { flagCode: 'CA', name: 'Canada' },
  { flagCode: 'FR', name: 'France' },
  { flagCode: 'JP', name: 'Japan' },
  { flagCode: 'AU', name: 'Australia' },
  { flagCode: 'SG', name: 'Singapore' },
]

const homeResourceLinks = [
  {
    title: 'Service quick start',
    description: 'Jump into proxy setup, routing, and request examples.',
    href: '/service#quick-start',
    icon: Code2,
  },
  {
    title: 'Coverage planning',
    description: 'Check priority markets and upcoming country availability.',
    href: '/coverage',
    icon: Globe2,
  },
  {
    title: 'Frequently asked questions',
    description: 'Answer pricing, routing, session, and support questions.',
    href: '/faq',
    icon: Search,
  },
  {
    title: 'Technical support',
    description: 'Share workflow details and get help choosing the right plan.',
    href: '/faq#faq-contact',
    icon: Headphones,
  },
]

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
  { logo: g2Logo, alt: 'G2', source: 'Reviewed on G2', value: '4.7/5', label: 'Independent Review Rating' },
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
  { value: '200+', label: 'Countries Covered', icon: Globe2 },
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
    title: 'Per-IP Packaging Teams Can Understand Quickly',
    description:
      'This is easier to compare than per-GB pricing when the real concern is continuity, not burst traffic.',
    metric: '$1.30',
    metricLabel: 'Entry Price per IP',
  },
  {
    kicker: '04',
    category: 'Proof Layer',
    icon: BadgeCheck,
    title: 'Proof Points Your Team Can Verify Quickly',
    description:
      'Compare the numbers that matter: pool size, countries, success rate, and routing controls before talking to sales.',
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
    cta: 'Choose Plan',
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
  { icon: Globe2, value: '200+', label: 'Countries and regions' },
  { icon: Clock3, value: '24h', label: 'Sticky session window' },
]

const pricingProductCategories = [
  {
    title: 'Static ISP Proxies',
    description:
      'Stable ISP-assigned identities for account workflows, price monitoring, scraping, and longer sessions.',
    status: 'Available now',
    cta: 'View pricing',
    href: '/pricing/static-isp-proxies',
    code: 'ISP',
    tone: 'isp',
    group: 'static',
    iconSvg: staticResidentialIcon,
    available: true,
    meta: ['From $1.30/IP', 'Sticky sessions', 'Country routing'],
  },
  {
    title: 'Residential Proxies',
    description:
      'Rotating residential IPs for high-volume public data collection and broad market coverage.',
    status: 'Coming soon',
    cta: 'Coming soon',
    href: '/pricing/residential-proxies',
    code: 'RP',
    tone: 'residential',
    group: 'dynamic',
    iconSvg: dynamicResidentialIcon,
    available: false,
    meta: ['Rotating pool', 'Global coverage', 'Public data'],
  },
  {
    title: 'Datacenter Proxies',
    description:
      'Fast server-hosted IPs for speed-sensitive tasks where residential trust is not required.',
    status: 'Coming soon',
    cta: 'Coming soon',
    href: '/pricing/datacenter-proxies',
    code: 'DC',
    tone: 'datacenter',
    group: 'dynamic',
    iconSvg: dynamicDatacenterIcon,
    available: false,
    meta: ['High throughput', 'Low latency', 'Bulk tasks'],
  },
  {
    title: 'Dedicated Datacenter Proxies',
    description:
      'Private datacenter routes for predictable performance, fixed allocation, and team-owned workflows.',
    status: 'Coming soon',
    cta: 'Coming soon',
    href: '/pricing/dedicated-datacenter-proxies',
    code: 'DDC',
    tone: 'dedicated-dc',
    group: 'static',
    iconSvg: staticDatacenterIcon,
    available: false,
    meta: ['Private IPs', 'Fixed allocation', 'Predictable speed'],
  },
  {
    title: 'Dedicated ISP Proxies',
    description:
      'Dedicated ISP inventory for teams that need cleaner trust signals and exclusive route planning.',
    status: 'Coming soon',
    cta: 'Coming soon',
    href: '/pricing/dedicated-isp-proxies',
    code: 'DIP',
    tone: 'dedicated-isp',
    group: 'static',
    iconSvg: staticResidentialIcon,
    available: false,
    meta: ['Exclusive routes', 'ISP identity', 'Workflow review'],
  },
  {
    title: 'Mobile Proxies',
    description:
      'Carrier-backed mobile IPs for app testing, ad verification, and mobile-first market checks.',
    status: 'Coming soon',
    cta: 'Coming soon',
    href: '/pricing/mobile-proxies',
    code: 'MP',
    tone: 'mobile',
    group: 'dynamic',
    iconSvg: mobileIcon,
    available: false,
    meta: ['Carrier routes', 'Mobile contexts', 'App testing'],
  },
]

const pricingIndexFaqItems = [
  {
    question: 'Which proxy type should I start with?',
    answer:
      'Start with Static ISP Proxies when the workflow needs stable identity, sticky sessions, account continuity, or repeated checks from the same market. Use rotating residential or mobile routes when each request can safely use a different identity.',
  },
  {
    question: 'Why is Static ISP pricing available first?',
    answer:
      'Static ISP inventory is available now with published per-IP plans, routing expectations, and support scope. Additional proxy categories will receive public plan details as packages are finalized.',
  },
  {
    question: 'Are the coming-soon proxy types available through sales?',
    answer:
      'Some residential, datacenter, dedicated, and mobile requirements can be reviewed with sales before public pricing is published. Share the target countries, volume, session needs, and use case so the team can confirm fit.',
  },
  {
    question: 'What is the difference between ISP and dedicated ISP proxies?',
    answer:
      'Static ISP plans are packaged for standard stable-session workflows. Dedicated ISP packages are designed for teams that need exclusive allocation, route review, or more controlled sourcing.',
  },
  {
    question: 'Will every proxy type use per-IP pricing?',
    answer:
      'Not necessarily. Static ISP packages are priced per IP. Other categories may use different units, such as bandwidth, private allocation size, carrier route, or custom enterprise terms.',
  },
  {
    question: 'Can I compare all proxy types before buying?',
    answer:
      'Yes. Compare the active Static ISP plans now, then contact support for a recommendation if your workflow may need another proxy type.',
  },
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
    cta: 'Choose Plan',
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
    description: 'Plan market-specific checks across 200+ countries and priority commercial regions.',
  },
  {
    icon: Headphones,
    title: 'Support for Scale',
    description: 'Premium and enterprise packages add onboarding, routing review, and account management.',
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
    description: 'Enterprise teams can request sourcing, privacy, and security materials during review.',
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
      'Enterprise and sensitive workflows may require additional review. ROLA-IP is intended for legitimate research, monitoring, verification, and automation use cases.',
  },
  {
    question: 'Are there restricted targets or use cases?',
    answer:
      'Yes. Fraud, spam, credential abuse, and high-risk account manipulation are not allowed. Teams should validate target policies before production rollout.',
  },
  {
    question: 'Can teams validate before scaling?',
    answer:
      'Teams can start with a small paid ISP proxy allocation to validate fit, while refund or procurement terms should be confirmed before checkout.',
  },
]

const coverageSummary = '200+ Countries'

const coverage = [
  { flagCode: 'US', name: 'United States', count: '5.4M+ IPs' },
  { flagCode: 'GB', name: 'United Kingdom', count: '110K+ IPs' },
  { flagCode: 'DE', name: 'Germany', count: '376K+ IPs' },
  { flagCode: 'FR', name: 'France', count: '190K+ IPs' },
  { flagCode: 'CA', name: 'Canada', count: '320K+ IPs' },
  { flagCode: 'AU', name: 'Australia', count: '95K+ IPs' },
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
    icon: SearchCheck,
    title: 'Market Research',
    description:
      'Collect location-sensitive pricing and catalog signals without the churn that often comes with aggressive rotation.',
    signal: 'Cleaner market snapshots',
  },
  {
    icon: ShieldCheck,
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
  { value: '200+', label: 'countries and regions' },
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
    metric: '200+',
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
      'Keep price, stock, seller, and buy-box checks tied to the same market context so repeated reads are comparable.',
    signal: 'Price, stock, seller drift',
  },
  {
    icon: ScanSearch,
    title: 'SEO and SERP Tracking',
    description:
      'Capture search results, ads, and rank positions from fixed countries without location drift between requests.',
    signal: 'SERP snapshots by market',
  },
  {
    icon: Bot,
    title: 'AI and LLM Training Data',
    description:
      'Run long public-data collection jobs with controlled retries, region diversity, and cleaner source attribution.',
    signal: 'Dataset quality control',
  },
  {
    icon: Megaphone,
    title: 'Ad Verification',
    description:
      'Verify geo delivery, landing-page redirects, and account-specific funnels from trusted residential routes.',
    signal: 'Geo delivery audit',
  },
  {
    icon: Search,
    title: 'Market Research',
    description:
      'Compare competitor pricing, catalog depth, ratings, and availability with less noise from aggressive rotation.',
    signal: 'Competitor signal tracking',
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

const scrapingAwards = [
  { label: 'G2 review signals', href: 'https://www.g2.com/products/rola-ip/reviews', external: true },
  { label: 'Trustpilot rating', href: 'https://www.trustpilot.com/search?query=rola-ip', external: true },
  { label: 'Enterprise onboarding', href: '/faq#faq-contact', external: false },
  { label: 'Security documentation', href: '/service#compliance', external: false },
]

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
      'Web scraping rules depend on the target, data type, jurisdiction, and collection method. ROLA-IP is intended for legitimate public data research, monitoring, and verification, and teams should review policies before rollout.',
  },
  {
    question: 'Which scraping scenarios benefit most from sticky ISP sessions?',
    answer:
      'E-commerce price intelligence, SEO and SERP tracking, ad verification, AI dataset collection, brand monitoring, and account-sensitive research often benefit from stable identity and predictable routing.',
  },
  {
    question: 'Do you provide a managed Web Scraping API?',
    answer:
      'ROLA-IP currently supports proxy-based scraping workflows. If you need managed rendering, retries, or structured output, contact support so we can review the requirement.',
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
      'Route by country, plan tier, and sticky-session key across 200+ markets without rebuilding endpoint logic.',
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
const openPricingIndexFaqIndex = ref(0)
const openPricingPageFaqIndex = ref(0)
const openFaqPageIndex = ref(0)
const faqPageSearch = ref('')
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

const openPricingIndexFaq = (index: number) => {
  openPricingIndexFaqIndex.value = index
}

const openPricingPageFaq = (index: number) => {
  openPricingPageFaqIndex.value = index
}

const openFaqPage = (index: number) => {
  openFaqPageIndex.value = index
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
  'Keep one IP for login, verification, and multi-step account flows.',
  'Plan cost by IP count instead of guessing bandwidth usage.',
  'Use it when rotating proxies cause re-login, captchas, or broken sessions.',
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
  { label: 'ISO 27001', image: iso27001Badge, alt: 'ISO 27001 information security visual', meta: 'Security review', tone: 'iso' },
  { label: 'SOC 2', image: soc2Badge, alt: 'SOC 2 audit visual', meta: 'Audit material', tone: 'soc' },
  { label: 'GDPR', image: gdprBadge, alt: 'GDPR privacy visual', meta: 'EU privacy', tone: 'gdpr' },
  { label: 'CCPA', image: ccpaBadge, alt: 'CCPA privacy notice visual', meta: 'CA privacy', tone: 'ccpa' },
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
    question: 'Can Teams Validate Before Scaling?',
    answer:
      'Teams can choose a small paid ISP proxy allocation to validate routing, session behavior, and target compatibility before moving into a larger plan.',
  },
  {
    question: 'How Does Billing Work?',
    answer:
      'Plans are presented with predictable per-IP pricing, so teams can estimate monthly cost by inventory size rather than relying only on bandwidth consumption.',
  },
  {
    question: 'Which Locations Are Supported?',
    answer:
      'ROLA-IP supports 200+ countries, with priority ISP inventory in the United States, United Kingdom, Germany, France, Canada, Australia, and other major commercial markets.',
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

type FaqQuestionCategoryKey = 'basics' | 'pricing' | 'routing' | 'compliance' | 'support'

const faqPageCategoryLabels: Record<FaqQuestionCategoryKey, string> = {
  basics: 'Basics',
  pricing: 'Pricing',
  routing: 'Routing',
  compliance: 'Compliance',
  support: 'Support',
}

const faqPageItems: Array<{
  id: string
  category: FaqQuestionCategoryKey
  question: string
  answer: string
}> = [
  {
    id: 'static-isp-proxy',
    category: 'basics',
    question: 'What is a static ISP proxy?',
    answer:
      'A static ISP proxy is an ISP-assigned IP that keeps the same online identity for longer sessions while carrying residential-style trust signals. It is useful when a workflow needs continuity across login, review, checkout, monitoring, or account-sensitive steps.',
  },
  {
    id: 'isp-vs-rotating',
    category: 'basics',
    question: 'What is the difference between static ISP and rotating residential proxies?',
    answer:
      'Static ISP proxies keep one consistent IP for session-sensitive work. Rotating residential proxies switch IPs on a schedule or per request, which is better for broad public collection where continuity is less important.',
  },
  {
    id: 'static-isp-use-cases',
    category: 'basics',
    question: 'What can I use static ISP proxies for?',
    answer:
      'Static ISP proxies are best for workflows that need a stable residential identity, such as account operations, ad verification, localized testing, market monitoring, and longer-running research tasks.',
  },
  {
    id: 'sticky-sessions',
    category: 'routing',
    question: 'Can I maintain long sessions with the same IP?',
    answer:
      'Yes. Static ISP proxies are designed for session continuity, so the same IP can stay attached to a workflow for longer interactions. ROLA-IP positions sticky sessions around up to 24-hour continuity, depending on routing and target behavior.',
  },
  {
    id: 'country-routing',
    category: 'routing',
    question: 'Can I choose country or market-level targeting?',
    answer:
      'Yes. Country-level routing is part of the core workflow. If you need specific markets, inventory availability, or a sensitive rollout plan, contact support so we can confirm the best route before production.',
  },
  {
    id: 'per-ip-pricing',
    category: 'pricing',
    question: 'How is pricing calculated for static ISP proxies?',
    answer:
      'ROLA-IP pricing is framed around static ISP packages per IP, not unpredictable per-GB usage. That makes planning easier when your main requirement is a stable inventory size and predictable monthly capacity.',
  },
  {
    id: 'start-small',
    category: 'pricing',
    question: 'Can I test the proxies before committing to a larger plan?',
    answer:
      'Yes. Start with a smaller allocation to validate routing, session stability, target compatibility, and support needs. Once the workflow is proven, you can expand inventory or move into a custom procurement path.',
  },
  {
    id: 'blocked-targets',
    category: 'routing',
    question: 'What happens if a target blocks or challenges traffic?',
    answer:
      'Start by checking route, session behavior, request pacing, and browser signals. Support can help review the workflow, but customers should also respect target policies and acceptable-use boundaries.',
  },
  {
    id: 'allowed-use',
    category: 'compliance',
    question: 'What use cases are allowed?',
    answer:
      'ROLA-IP is intended for legitimate research, monitoring, verification, automation, and market intelligence workflows. Fraud, spam, credential abuse, and high-risk account manipulation are not allowed.',
  },
  {
    id: 'security-review',
    category: 'compliance',
    question: 'Can enterprise teams request security or sourcing documents?',
    answer:
      'Yes. Enterprise and procurement-led teams can request security, sourcing, privacy, and commercial documentation during review.',
  },
  {
    id: 'kyc-review',
    category: 'compliance',
    question: 'Do some workflows require additional review?',
    answer:
      'Sensitive or enterprise workflows may require additional review before approval. That review helps align routing, acceptable-use expectations, and commercial terms before launch.',
  },
  {
    id: 'onboarding-help',
    category: 'support',
    question: 'What onboarding help is available?',
    answer:
      'Teams can get help with endpoint setup, country routing, sticky-session patterns, and validation steps. Premium and enterprise packages include a clearer support path for larger deployments.',
  },
  {
    id: 'upgrade-plan',
    category: 'support',
    question: 'Can we upgrade after validating a workflow?',
    answer:
      'Yes. The recommended path is to validate one serious workflow first, then expand inventory, support level, and procurement terms once the route and session pattern are proven.',
  },
  {
    id: 'sales-info',
    category: 'support',
    question: 'What details should we bring when talking to sales?',
    answer:
      'Bring target countries, expected session length, traffic volume, target workflow, compliance requirements, and whether you need invoice, sourcing, or security review support.',
  },
]

const getFaqPageCategoryLabel = (key: FaqQuestionCategoryKey) => faqPageCategoryLabels[key]

const normalizedFaqPageSearch = computed(() => faqPageSearch.value.trim().toLowerCase())

const filteredFaqPageItems = computed(() =>
  faqPageItems.filter((item) => {
    const searchableText = `${item.question} ${item.answer} ${getFaqPageCategoryLabel(item.category)}`.toLowerCase()
    const matchesSearch = !normalizedFaqPageSearch.value || searchableText.includes(normalizedFaqPageSearch.value)

    return matchesSearch
  }),
)

const visibleFaqPageItems = computed(() =>
  normalizedFaqPageSearch.value ? filteredFaqPageItems.value : faqPageItems.slice(0, 7),
)

const isPlaceholder = (value: string) => value.startsWith('[')
const flagIcon = (code: string) => `/flags/${code.toUpperCase()}.svg`
</script>
