// components/layout/AppHeader.vue
<template>
  <header class="bg-white border-b border-gray-200">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <!-- Mobile menu button -->
        <div class="flex items-center md:hidden">
          <button
            @click="$emit('toggleSidebar')"
            type="button"
            class="inline-flex items-center justify-center rounded-md p-2 text-gray-700 hover:bg-gray-100"
          >
            <Bars3Icon class="h-6 w-6" />
          </button>
        </div>

        <!-- Search -->
        <div class="flex flex-1 items-center justify-center md:justify-start">
          <div class="w-full max-w-lg lg:max-w-xs">
            <label for="search" class="sr-only">Search courses</label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" />
              </div>
              <input
                id="search"
                name="search"
                class="block w-full rounded-md border-0 bg-white py-1.5 pl-10 pr-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Search courses..."
                type="search"
              >
            </div>
          </div>
        </div>

        <!-- Right side icons -->
        <div class="flex items-center gap-4">
          <!-- Notifications -->
          <button type="button" class="relative rounded-full p-1 text-gray-600 hover:text-gray-900">
            <span class="sr-only">View notifications</span>
            <BellIcon class="h-6 w-6" />
            <span class="absolute -top-1 -right-1 h-4 w-4 rounded-full bg-red-500 text-xs text-white flex items-center justify-center">
              2
            </span>
          </button>

          <!-- Profile dropdown -->
          <div class="relative">
            <button
              @click="isProfileOpen = !isProfileOpen"
              type="button"
              class="flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
            >
              <img
                class="h-8 w-8 rounded-full"
                src="/api/placeholder/32/32"
                alt="User profile"
              >
            </button>

            <!-- Dropdown menu -->
            <div v-if="isProfileOpen" class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5">
              <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Your Profile</a>
              <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Settings</a>
              <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Sign out</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { Bars3Icon, BellIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

const isProfileOpen = ref(false)

defineEmits(['toggleSidebar'])
</script>


