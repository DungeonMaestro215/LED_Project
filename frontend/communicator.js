// window.onload = () => {
//     document.getElementById('hello').addEventListener('click', clickHandler);
// }

const communicator = async function(effect) {
    const result = await axios({
        method: 'get',
        url: 'http://192.168.0.118:3000/',
        params: {
            effect: effect,
            args: effect.getArgumentList()
        }
    });
    console.log(result);
}
