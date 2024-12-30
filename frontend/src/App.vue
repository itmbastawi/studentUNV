// App.vue
<template>
  <div class="h-screen flex overflow-hidden bg-gray-100">
    <!-- Sidebar -->
    <AppSidebar :is-open="isSidebarOpen" @close="isSidebarOpen = false" />

    <!-- Main content -->
    <div class="flex flex-col w-0 flex-1 overflow-hidden">
      <AppHeader @toggle-sidebar="isSidebarOpen = !isSidebarOpen" />

      <main class="flex-1 relative overflow-y-auto focus:outline-none">
        <div class="py-6">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
            <router-view></router-view>
          </div>
        </div>
      </main>

      <AppFooter />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from '@/components/layout/AppHeader.vue'
import AppSidebar from '@/components/layout/AppSidebar.vue'
import AppFooter from '@/components/layout/AppFooter.vue'

const isSidebarOpen = ref(false)
</script>

// components/layout/AppSidebar.vue
<template>
  <div>
    <!-- Mobile sidebar backdrop -->
    <div v-if="isOpen" 
         class="fixed inset-0 z-40 flex md:hidden"
         @click="$emit('close')">
      <div class="fixed inset-0 bg-gray-600 bg-opacity-75"></div>
    </div>

    <!-- Sidebar -->
    <div :class="[
      'fixed inset-y-0 left-0 flex flex-col w-64 bg-white border-r transform transition-transform duration-300 ease-in-out z-50',
      isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
    ]">
      <!-- Logo -->
      <div class="flex items-center justify-center h-16 px-4 bg-indigo-600">
        <img class="h-8 w-auto" src="@/assets/logo.svg" alt="Logo" />
      </div>

      <!-- Navigation -->
      <nav class="flex-1 px-2 py-4 space-y-1">
        <router-link v-for="item in navigationItems" 
                    :key="item.path"
                    :to="item.path"
                    :class="[
                      isActivePath(item.path)
                        ? 'bg-indigo-50 text-indigo-600'
                        : 'text-gray-600 hover:bg-gray-50',
                      'group flex items-center px-2 py-2 text-sm font-medium rounded-md'
                    ]">
          <component :is="item.icon" 
                    :class="[
                      isActivePath(item.path)
                        ? 'text-indigo-600'
                        : 'text-gray-400 group-hover:text-gray-500',
                      'mr-3 h-6 w-6'
                    ]" />
          {{ item.name }}
        </router-link>
      </nav>

      <!-- User Profile -->
      <div class="flex-shrink-0 flex border-t border-gray-200 p-4">
        <div class="flex-shrink-0 w-full group block">
          <div class="flex items-center">
            <div class="ml-3">
              <p class="text-sm font-medium text-gray-700">Admin User</p>
              <p class="text-xs font-medium text-gray-500">View Profile</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import {
  HomeIcon,
  AcademicCapIcon,
  UsersIcon,
  ChartBarIcon,
  CogIcon
} from '@heroicons/vue/outline'

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  }
})

defineEmits(['close'])

const route = useRoute()

const navigationItems = [
  { name: 'Dashboard', path: '/', icon: HomeIcon },
  { name: 'Courses', path: '/courses', icon: AcademicCapIcon },
  { name: 'Students', path: '/students', icon: UsersIcon },
  { name: 'Analytics', path: '/analytics', icon: ChartBarIcon },
  { name: 'Settings', path: '/settings', icon: CogIcon }
]

const isActivePath = (path) => route.path === path
</script>

// components/layout/AppHeader.vue
<template>
  <header class="bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <!-- Left section -->
        <div class="flex">
          <button
            @click="$emit('toggle-sidebar')"
            class="px-4 border-r border-gray-200 text-gray-500 md:hidden">
            <span class="sr-only">Open sidebar</span>
            <MenuIcon class="h-6 w-6" />
          </button>
          <div class="flex-1 flex items-center px-4">
            <h1 class="text-lg font-semibold text-gray-900">
              {{ currentPageTitle }}
            </h1>
          </div>
        </div>

        <!-- Right section -->
        <div class="flex items-center">
          <!-- Search -->
          <div class="flex-1 flex items-center justify-center px-2 lg:ml-6 lg:justify-end">
            <div class="max-w-lg w-full lg:max-w-xs">
              <label for="search" class="sr-only">Search</label>
              <div class="relative">
                <input
                  id="search"
                  type="text"
                  placeholder="Search"
                  class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                />
              </div>
            </div>
          </div>

          <!-- Notifications -->
          <button class="ml-6 p-1 rounded-full text-gray-400 hover:text-gray-500">
            <span class="sr-only">View notifications</span>
            <BellIcon class="h-6 w-6" />
          </button>

          <!-- Profile dropdown -->
          <div class="ml-3 relative">
            <button
              class="max-w-xs bg-white flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              <span class="sr-only">Open user menu</span>
              <img
                class="h-8 w-8 rounded-full"
                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                alt=""
              />
            </button>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { MenuIcon, BellIcon } from '@heroicons/vue/outline'

defineEmits(['toggle-sidebar'])

const route = useRoute()

const currentPageTitle = computed(() => {
  const pathToTitle = {
    '/': 'Dashboard',
    '/courses': 'Course Management',
    '/students': 'Student List',
    '/analytics': 'Analytics',
    '/settings': 'Settings'
  }
  return pathToTitle[route.path] || 'Dashboard'
})
</script>

// components/layout/AppFooter.vue
<template>
  <footer class="bg-white border-t border-gray-200">
    <div class="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center">
        <div class="text-sm text-gray-500">
          © 2024 E-Learning Platform. All rights reserved.
        </div>
        <div class="flex space-x-6">
          <a href="#" class="text-sm text-gray-500 hover:text-gray-900">Privacy Policy</a>
          <a href="#" class="text-sm text-gray-500 hover:text-gray-900">Terms of Service</a>
          <a href="#" class="text-sm text-gray-500 hover:text-gray-900">Contact Support</a>
        </div>
      </div>
    </div>
  </footer>
</template>

// router/index.js
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue')
  },
  {
    path: '/courses',
    name: 'Courses',
    component: () => import('@/views/CourseManagement.vue')
  },
  {
    path: '/students',
    name: 'Students',
    component: () => import('@/views/StudentList.vue')
  },
  {
    path: '/analytics',
    name: 'Analytics',
    component: () => import('@/views/Analytics.vue')
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('@/views/Settings.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router