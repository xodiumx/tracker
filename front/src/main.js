import './assets/main.css'

import TrackerComponent from '@/components/TrackerComponent.vue'
import TaskComponent from '@/components/TaskComponent.vue'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

app.mount('#app')
app.component('TrackerComponent', TrackerComponent)
app.component('TaskComponent', TaskComponent)