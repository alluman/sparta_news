<template>
<div class="signup-login">
    <h2>Login / Signup</h2>
    <form @submit.prevent="submitForm">
    <input v-model="username" type="text" placeholder="Username">
    <input v-model="password" type="password" placeholder="Password">
    <button type="submit">Submit</button>
    </form>
</div>
</template>

<script>
export default {
name: 'SignupLogin',
data() {
    return {
    username: '',
    password: ''
    };
},
methods: {
    submitForm() {
    alert(`Username: ${this.username}, Password: ${this.password}`);
    }
}
};
</script>

<style scoped>
.signup-login form {
display: flex;
flex-direction: column;
}
.signup-login input,
.signup-login button {
margin-top: 10px;
}
</style>
