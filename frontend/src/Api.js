const API = {

    login: (data) => {
        return new Promise((resolve, reject) => {
            fetch('/api/token-auth/', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            .then(resp => {
                let json = resp.json()
                if (resp.status !== 200) {
                    console.log(json);
                    reject(json);
                }
                return json
            })
            .then(json => {
                localStorage.setItem('token', json.token);
                resolve(json.user);
            })
            .catch(error => {
                reject(error);
            });
        });
    },

    signup: (data) => {
        return new Promise((resolve, reject) => {
            fetch('/api/users/', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            .then(resp => {
                let json = resp.json()
                if (resp.status !== 201) {
                    console.log(json);
                    reject(json);
                }
                return json
            })
            .then(json => {
                localStorage.setItem('token', json.token);
                resolve(json);
            })
            .catch(error => {
                reject(error);
            });
        });
    },

    logout: () => {
        try {
            localStorage.removeItem('token');
            return false;
        } catch (e) {
            console.log(e);
        }
    },

    fetchTaskList: async () => {
        try {
            const response = await fetch('/api/tasks/', {
                headers: {
                    'Authorization': 'JWT ' + localStorage.getItem('token')
                }
            })
            if (response.status === 401) {
                window.location.replace('/')
            }
            const json = await response.json()
            return json
        } catch (e) {
            console.log(e);
        }
    },

    postNewTask: async (task) => {
        try {
            const response = await fetch('/api/tasks/', {
                method: 'POST',
                body: JSON.stringify(task),
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'JWT ' + localStorage.getItem('token')
                },
            })
            if (response.status === 401) {
                window.location.replace('/')
            }
            const json = await response.json()
            return json
        } catch (e) {
            console.log(e);
        }
    }

}

export default API;
