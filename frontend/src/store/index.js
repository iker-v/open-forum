import Vuex from 'vuex'
import axios from 'axios'

export default new Vuex.Store({
    state:{
        store: 'ssdfsdfsd',
        searchThread: {
            isSearching: false,
            isLoading: false,
            query: '',
            result: [],
        },
        auth: {
            showLogin: false,
            showRegister: false,
            profile_pic: '',
            username: '',
            email: '',
            password: '',
            token: '',
            isAuthenticated: false,
        }
    },
    mutations:{
        searchThread(state){
            state.searchThread.isSearching = true
            state.searchThread.isLoading = true
            axios.get(`/search-thread/${searchThread.query}`)
            .then((response) => {
                state.searchThread.result = response['threads']
            })
            .finally(() => state.searchThread.isLoading = false)
        },
        changeSearchQuery(state, value){
            state.searchThread.query = value
        },
        changeShowSearch(state){
            state.searchThread.isSearching = !state.searchThread.isSearching
        },
        changeShowRegister(state){
            state.auth.showRegister = !state.auth.showRegister
        },
        changeShowLogin(state){
            state.auth.showLogin = !state.auth.showLogin
        },
        initializeStore(state){
            if (localStorage.getItem('token')) {
                state.auth.token = localStorage.getItem('token')
                state.auth.isAuthenticated = true
                axios.defaults.headers.common["Authorization"] = "Token " + state.auth.token
            } else {
                state.auth.token = ''
                axios.defaults.headers.common["Authorization"] = ''
                state.auth.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.auth.token = token
        },
        setUser(state, username){
            state.auth.username = username
            localStorage.setItem("username", username)
        },
        removeToken(state){
            localStorage.removeItem("token")
            state.auth.token = ''
            state.auth.isAuthenticated = false
        }
    },
    actions:{

    }
})