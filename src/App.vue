<template>
  <div ref="pageRoot" class="site-page">
    <header class="site-header" :class="{ 'site-header--scrolled': isHeaderScrolled }" aria-label="Primary">
      <div class="container site-header__inner">
        <a class="brand" href="#top" aria-label="rola-ip home">
          <img class="brand__logo" :src="brandLogo" alt="rola-ip" />
        </a>

        <nav class="site-nav" aria-label="Section navigation">
          <a v-for="item in navItems" :key="item.label" :href="item.href">{{ item.label }}</a>
        </nav>

        <div class="site-actions">
          <a class="button button--ghost" href="#faq">Talk to Sales</a>
          <a class="button button--primary" href="#pricing">Start Free Trial</a>
        </div>
      </div>
    </header>

    <main id="top">
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
let scrollAnimationContext: ReturnType<typeof gsap.context> | undefined
let handleHeaderScroll: (() => void) | undefined

onMounted(() => {
  handleHeaderScroll = () => {
    isHeaderScrolled.value = window.scrollY > 16
  }
  handleHeaderScroll()
  window.addEventListener('scroll', handleHeaderScroll, { passive: true })

  if (!pageRoot.value || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return
  }

  scrollAnimationContext = gsap.context(() => {
    gsap.set(
      [
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
        '.faq-item',
      ],
      { willChange: 'transform, opacity' },
    )

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

    gsap.utils
      .toArray<HTMLElement>(
        '.proof-panel, .performance-layout, .pricing-card, .coverage-card, .network-card, .quick-start-card, .feature-card, .testimonial-card, .compliance-panel, .faq-item',
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

  }, pageRoot.value)
})

onUnmounted(() => {
  if (handleHeaderScroll) {
    window.removeEventListener('scroll', handleHeaderScroll)
  }
  scrollAnimationContext?.revert()
})

const navItems = [
  { label: 'Features', href: '#features' },
  { label: 'Pricing', href: '#pricing' },
  { label: 'Coverage', href: '#coverage' },
  { label: 'Use Cases', href: '#use-cases' },
  { label: 'FAQ', href: '#faq' },
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
  'https://api.dicebear.com/10.x/fun-emoji/svg?seed=RolaResearchLead',
  'https://api.dicebear.com/10.x/fun-emoji/svg?seed=RolaOpsLead',
  'https://api.dicebear.com/10.x/fun-emoji/svg?seed=RolaGrowthLead',
  'https://api.dicebear.com/10.x/fun-emoji/svg?seed=RolaAutomationLead',
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
