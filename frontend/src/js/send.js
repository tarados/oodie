import axios from "axios";

export async function get(endpoint) {
    const url = `${process.env.VUE_APP_API}/${endpoint}`;
    const response = await axios.get(url);
    if (response.status === 200) {
        return response.data;
    }
    return null;
}

export async function post(endpoint, data) {
    const url = `${process.env.VUE_APP_API}/${endpoint}`;
    const response = await axios.post(url, data);
    if (response.status === 200) {
        return response.data;
    }
    return null;
}
