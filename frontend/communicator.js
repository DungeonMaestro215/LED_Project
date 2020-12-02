window.onload = () => {
    document.getElementById('hello').addEventListener('click', clickHandler);
}

const clickHandler = async function(e) {
    const result = await axios({
        method: 'get',
        url: 'http://localhost:3000/',
        params: {
            id: 14
        }
    });
    console.log(result);
}