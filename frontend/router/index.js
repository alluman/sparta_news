import { createRouter, createWebHistory } from 'vue-router';
import MainHome from '../src/views/MainHome.vue';
import DetailPage from '../src/views/DetailPage.vue';
import CommentsPage from '../src/views/CommentsPage.vue';
import SignupLoginPage from '../src/views/SignupLoginPage.vue';
import UserProfilePage from '../src/views/UserProfilePage.vue';
import PostsPage from '../src/views/PostsPage.vue';

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: [
    { path: '/', name: 'home', component: MainHome },
    { path: '/post/:id', name: 'detail', component: DetailPage },
    { path: '/comments', name: 'comments', component: CommentsPage },
    { path: '/signup-login', name: 'signup-login', component: SignupLoginPage },
    { path: '/user-profile', name: 'user-profile', component: UserProfilePage },
    { path: '/posts', name: 'posts', component: PostsPage }
    ]
});

export default router;