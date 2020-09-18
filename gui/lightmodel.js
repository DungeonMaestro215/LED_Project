let LEDModel = class {
    constructor(num_leds) {
        this.num_leds = num_leds;
        this.pixels = [];
        this.listeners = [];

        // Initialize off LEDs
        for (let i = 0; i < num_leds; i++) {
            this.pixels[i] = new Pixel(0, 0, 0, i);
        }
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

};

let Pixel = class {
    constructor(r, g, b, id) {
        this.r = r;
        this.g = g;
        this.b = b;
        this.id = id;
        this.listeners = [];
    }

    changeColor(r, g, b) {
        this.r = r;
        this.g = g;
        this.b = b;
        this.updateListeners(this);
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