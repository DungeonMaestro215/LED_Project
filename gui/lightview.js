let LEDView = class {
    constructor(model) {
        this.model = model;
        this.listeners = [];
        this.div = document.createElement("div");

        let led_strip = document.createElement("div");
        led_strip.setAttribute("class", "strip");

        let pixel_click_handler = (e) => {
            // TODO

            let pix = e.target;
            this.updateListeners({
                action: "click",
                id: pix.data_model.id,
                color: {
                    r: 150,
                    g: 0,
                    b: 0
                }
            });
        }

        for (let i = 0; i < model.num_leds; i++) {
            let pixel_view = new PixelView(model.pixels[i]);
            pixel_view.div.addEventListener("click", pixel_click_handler);
            led_strip.appendChild(pixel_view.div);
        }

        this.div.appendChild(led_strip);

        // When model updates, do something to this view
        this.model.addListener((e) => {
            // TODO
        });
    }

    addListener(listener) {
        let idx = this.listeners.findIndex((l) => l == listener);
        if (idx == -1) {
            this.listeners.push(listener);
        }
    }

    removeListener(listener) {
        let idx = this.listeners.findIndex((l) => l == listener);
        if (idx != -1) {
            this.listeners.splice(idx, 1);
        }
    }

    updateListeners(event) {
        this.listeners.forEach((l) => l(event));
    }

}

let PixelView = class {
    constructor(pixel_model) {
        this.div = document.createElement("div");
        this.div.setAttribute("class", "pixel box");
        this.div.data_model = pixel_model;      // Internet warns of possible future namespace collisions, but this works for now
        this.div.style.backgroundColor = `rgb(${pixel_model.r}, ${pixel_model.g}, ${pixel_model.b})`;

        // When model updates, do something to this view.
        pixel_model.addListener(() => {
            this.update();
        });
    }
    
    update() {
        let pix = this.div.data_model;
        this.div.style.backgroundColor = `rgb(${pix.r}, ${pix.g}, ${pix.b})`;
    }

}