
// components/layout/AppFooter.vue
<template>
  <footer class="bg-white border-t border-gray-200">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col items-center md:flex-row md:justify-between py-4">
        <!-- Left section -->
        <div class="text-center md:text-left mb-4 md:mb-0">
          <p class="text-sm text-gray-500">
            © {{ currentYear }} EduLearn Platform. All rights reserved.
          </p>
        </div>

        <!-- Right section -->
        <nav class="flex space-x-6">
          <a
            v-for="link in footerLinks"
            :key="link.name"
            :href="link.href"
            class="text-sm text-gray-500 hover:text-gray-900"
          >
            {{ link.name }}
          </a>
        </nav>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())

const footerLinks = [
  { name: 'Privacy Policy', href: '#' },
  { name: 'Terms of Service', href: '#' },
  { name: 'Contact Support', href: '#' },
  { name: 'Documentation', href: '#' }
]
</script>