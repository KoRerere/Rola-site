<template>
  <footer class="service-footer" aria-labelledby="service-footer-title">
    <div class="container service-footer__inner">
      <div class="service-footer__grid">
        <section class="service-footer__column service-footer__company" aria-labelledby="service-footer-company">
          <h2 id="service-footer-company" class="service-footer__title">Pages</h2>
          <ul class="service-footer__links">
            <li v-for="link in footerCompanyLinks" :key="link.label">
              <a class="service-footer__link" :href="link.href">{{ link.label }}</a>
            </li>
          </ul>
        </section>

        <section class="service-footer__column service-footer__resources" aria-labelledby="service-footer-title">
          <div class="service-footer__resources-head">
            <h2 id="service-footer-title" class="service-footer__title">Partner Links</h2>
            <span>{{ footerPartnerLinks.length }} resources</span>
          </div>
          <div class="service-footer__resource-grid" aria-label="Partner resources">
            <span v-for="link in footerPartnerLinks" :key="link" class="service-footer__resource-link">
              {{ link }}
            </span>
          </div>
        </section>

        <address class="service-footer__contact" aria-label="ROLA-IP contact information">
          <p class="service-footer__contact-kicker">Contact</p>
          <a class="service-footer__phone" href="tel:+141353477">
            <PhoneCall aria-hidden="true" :size="22" :stroke-width="1.9" />
            <span><span class="service-footer__phone-code">+1</span>&nbsp;413&nbsp;534&nbsp;77</span>
          </a>
          <a class="service-footer__email" href="mailto:support@rola-ip.com">
            <Mail aria-hidden="true" :size="17" :stroke-width="2.1" />
            Email: support@rola-ip.com
          </a>
          <p class="service-footer__address">
            <MapPin aria-hidden="true" :size="18" :stroke-width="2.2" />
            <span>2307 Beverley Rd Brooklyn, New York 11226 United States.</span>
          </p>
          <a
            class="service-footer__directions"
            href="https://www.google.com/maps/search/?api=1&query=2307+Beverley+Rd+Brooklyn+New+York+11226"
            target="_blank"
            rel="noreferrer"
          >
            Get Directions
            <SquareArrowOutUpRight aria-hidden="true" :size="15" :stroke-width="2.2" />
          </a>

          <div class="service-footer__socials" aria-label="Social media links">
            <a
              v-for="social in footerSocialLinks"
              :key="social.label"
              class="service-footer__social-link"
              :href="social.href"
              target="_blank"
              rel="noreferrer"
              :aria-label="social.label"
            >
              <svg :viewBox="social.viewBox" aria-hidden="true" focusable="false">
                <path v-for="path in social.paths" :key="path" :d="path" fill="currentColor" />
              </svg>
              <span class="sr-only">{{ social.label }}</span>
            </a>
          </div>
        </address>
      </div>

      <div class="service-footer__bottom">
        <p>Copyright © 2026.ROLA-IP All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { Mail, MapPin, PhoneCall, SquareArrowOutUpRight } from '@lucide/vue'

const footerCompanyLinks = [
  { label: 'Service', href: '/' },
  { label: 'Features', href: '/use-cases' },
  { label: 'Pricing', href: '/pricing' },
  { label: 'Coverage', href: '/coverage' },
  { label: 'FAQ', href: '/faq' },
]

const footerPartnerLinks = [
  '最强云手机',
  'Twitter群推王',
  '鲁班跨境通',
  '向前论坛',
  '大数跨境',
  'YinoLink易诺',
  '邦阅网',
  '小U出海',
  '贝远导航',
  'ClonBrowser',
  '深圳的阳',
  '光子波动网',
  'IxBrowser',
  '创蓝论坛',
  '花漾浏览器',
  '海关数据查询平台',
  'VMLogin Antidetect Browser',
  '蓝鲸跨境',
  'Milohelp独立站搭建',
  'ZVCARD出海导航',
  'ISellerPal数派跨境',
  '易推广(亚马逊站外推广)',
  'TRACK718全球物流轨迹查询平台',
  '跨境365知识圈',
  '跨付KF',
  '顺风船独立站增长',
  '奇赞工具',
  '跨境服务商点评#5840',
  'Deal说（亚马逊站外推广）',
  'TKQNR跨境运营导航',
  '蓝色星期五',
  '易派Epay',
  'Sharklogin Antidetect Browser',
]

const footerSocialLinks = [
  {
    label: 'X',
    href: 'https://x.com/',
    viewBox: '0 0 24 24',
    paths: [
      'M18.244 2.25h3.308l-7.227 8.26 8.502 11.24h-6.657l-5.214-6.817-5.966 6.817H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77Z',
    ],
  },
  {
    label: 'LinkedIn',
    href: 'https://www.linkedin.com/',
    viewBox: '0 0 24 24',
    paths: [
      'M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.85-3.037-1.852 0-2.136 1.446-2.136 2.94v5.666H9.353V9h3.414v1.561h.049c.476-.9 1.637-1.85 3.37-1.85 3.602 0 4.267 2.371 4.267 5.455v6.286h-.006ZM5.337 7.433a2.063 2.063 0 1 1 0-4.126 2.063 2.063 0 0 1 0 4.126ZM7.119 20.452H3.554V9h3.565v11.452Z',
    ],
  },
  {
    label: 'Facebook',
    href: 'https://www.facebook.com/',
    viewBox: '0 0 24 24',
    paths: [
      'M22 12.061C22 6.477 17.523 2 11.939 2S2 6.477 2 12.061c0 5.045 3.693 9.229 8.522 9.988v-7.066H7.95v-2.922h2.572V9.833c0-2.537 1.511-3.94 3.824-3.94 1.108 0 2.267.198 2.267.198v2.493h-1.277c-1.258 0-1.65.781-1.65 1.581v1.896h2.807l-.449 2.922h-2.358v7.066C18.307 21.29 22 17.106 22 12.061Z',
    ],
  },
  {
    label: 'YouTube',
    href: 'https://www.youtube.com/',
    viewBox: '0 0 24 24',
    paths: [
      'M23.5 6.2a3.008 3.008 0 0 0-2.117-2.13C19.52 3.563 12 3.563 12 3.563s-7.52 0-9.383.508A3.008 3.008 0 0 0 .5 6.2 31.38 31.38 0 0 0 0 12a31.38 31.38 0 0 0 .5 5.8 3.008 3.008 0 0 0 2.117 2.13c1.863.507 9.383.507 9.383.507s7.52 0 9.383-.508A3.008 3.008 0 0 0 23.5 17.8c.337-1.867.5-3.734.5-5.8a31.38 31.38 0 0 0-.5-5.8ZM9.545 15.568V8.432L15.818 12l-6.273 3.568Z',
    ],
  },
  {
    label: 'GitHub',
    href: 'https://github.com/',
    viewBox: '0 0 24 24',
    paths: [
      'M12 .5C5.648.5.5 5.648.5 12c0 5.088 3.292 9.397 7.86 10.922.575.106.785-.25.785-.555 0-.274-.01-1-.016-1.962-3.197.694-3.872-1.542-3.872-1.542-.523-1.329-1.277-1.683-1.277-1.683-1.044-.714.08-.699.08-.699 1.154.081 1.762 1.185 1.762 1.185 1.026 1.757 2.69 1.25 3.346.956.104-.743.402-1.25.731-1.537-2.552-.29-5.235-1.276-5.235-5.68 0-1.255.448-2.281 1.184-3.085-.119-.291-.513-1.46.113-3.044 0 0 .966-.309 3.165 1.179A11.03 11.03 0 0 1 12 6.068c.978.004 1.964.132 2.884.387 2.198-1.488 3.163-1.179 3.163-1.179.627 1.584.233 2.753.114 3.044.737.804 1.183 1.83 1.183 3.085 0 4.415-2.687 5.386-5.247 5.671.413.355.78 1.057.78 2.131 0 1.538-.014 2.779-.014 3.156 0 .308.207.666.792.553C20.213 21.389 23.5 17.084 23.5 12 23.5 5.648 18.352.5 12 .5Z',
    ],
  },
  {
    label: 'Telegram',
    href: 'https://t.me/',
    viewBox: '0 0 24 24',
    paths: [
      'M21.94 4.25c.31-1.27-.83-2.34-2.04-1.86L2.66 9.17c-1.18.46-1.16 2.12.03 2.55l4.4 1.59 1.7 5.48c.36 1.17 1.84 1.52 2.69.64l2.43-2.5 4.38 3.2c1.02.75 2.47.19 2.75-1.05l2.9-14.83ZM8.25 12.6l8.65-5.32c.42-.26.85.31.49.64l-7.13 6.55-.28 3.04-1.73-4.91Zm2.92 5.17.2-2.18 1.4 1.02-1.6 1.16Z',
    ],
  },
]
</script>
