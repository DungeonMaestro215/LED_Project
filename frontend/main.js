window.onload = () => {
    const view = new View();
    // document.getElementById('hello').addEventListener('click', communicator);
    document.getElementById('apply').addEventListener('click', () => communicator(view.effect));
    document.getElementById('apply').addEventListener('click', () => console.log(view.effect));
}