let model = null;
let view = null;
let control = null;

window.onload = () => {
    // Setup MVC
    model = new LEDModel(300);
    view = new LEDView(model);
    control = new LEDController(model, view);

    // Load into DOM
    document.querySelector('#root').append(view.div);
};