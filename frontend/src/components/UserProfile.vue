<template>
    <div>
    <h1>User Profile</h1>
    <form @submit.prevent="updateProfile">
    <input type="password" v-model="password" placeholder="Password">
    <input type="email" v-model="email" placeholder="Email">
    <textarea v-model="introduction" placeholder="Introduce Yourself"></textarea>
    <button type="submit">Update Profile</button>
    </form>
</div>
</template>

<script>
export default {
data() {
    return {
    password: '',
    email: '',
    introduction: ''
    };
},
methods: {
    updateProfile() {
    console.log("Updating profile:", this.password, this.email, this.introduction);
    // Add logic to update profile
    }
}
};
</script>