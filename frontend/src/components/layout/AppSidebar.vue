
// components/layout/AppSidebar.vue

<template>
  <aside :class="[
    'fixed inset-y-0 left-0 z-50 w-64 transform transition-transform duration-300 ease-in-out bg-white border-r border-gray-200',
    isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
  ]">
    <!-- Logo -->
    <div class="h-16 flex items-center justify-center border-b border-gray-200">
      <img class="h-8" src="/api/placeholder/32/32" alt="Logo" />
      <span class="ml-2 text-xl font-bold text-gray-900">EduLearn</span>
    </div>

    <!-- Navigation -->
    <nav class="px-3 py-4">
      <div class="space-y-1">
        <router-link
          v-for="item in navigation"
          :key="item.name"
          :to="item.to"
          :class="[
            item.to === currentPath
              ? 'bg-indigo-50 text-indigo-600'
              : 'text-gray-700 hover:bg-gray-50',
            'group flex items-center px-3 py-2 rounded-md text-sm font-medium'
          ]"
        >
          <component
            :is="item.icon"
            :class="[
              item.to === currentPath ? 'text-indigo-600' : 'text-gray-400 group-hover:text-gray-500',
              'mr-3 h-5 w-5'
            ]"
          />
          {{ item.name }}
        </router-link>
      </div>
    </nav>

    <!-- User section -->
    <div class="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-200">
      <div class="flex items-center">
        <img class="h-8 w-8 rounded-full" src="/api/placeholder/32/32" alt="User" />
        <div class="ml-3">
          <p class="text-sm font-medium text-gray-700">John Doe</p>
          <p class="text-xs text-gray-500">Administrator</p>
        </div>
      </div>
    </div>

    <!-- Mobile close button -->
    <button
      v-if="isOpen"
      @click="$emit('close')"
      class="md:hidden absolute top-4 right-4 p-2 text-gray-500 hover:text-gray-900"
    >
      <XMarkIcon class="h-6 w-6" />
    </button>
  </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import {
  HomeIcon,
  AcademicCapIcon,
  UsersIcon,
  ChartBarIcon,
  Cog6ToothIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  }
})

defineEmits(['close'])

const route = useRoute()
const currentPath = computed(() => route.path)

const navigation = [
  { name: 'Dashboard', to: '/', icon: HomeIcon },
  { name: 'Courses', to: '/courses', icon: AcademicCapIcon },
  { name: 'Students', to: '/students', icon: UsersIcon },
  { name: 'Analytics', to: '/analytics', icon: ChartBarIcon },
  { name: 'Settings', to: '/settings', icon: Cog6ToothIcon }
]
</script>