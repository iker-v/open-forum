import axios from "axios"
import { category } from "./config"

export default {
    getCategories(){
        return axios.get(`${category}/get-categories`)
    }
}