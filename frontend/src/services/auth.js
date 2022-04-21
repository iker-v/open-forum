import axios from 'axios';

export default {
    register(username, email, password){
        const formData = {
            username: username,
            email: email,
            password: password
        }

        return axios.post("/account/users/", formData)
    },
    login(email, password){
        const formData = {
            email: email,
            password: password
        }

        return axios.post("/account/token/login/", formData)
    }
}