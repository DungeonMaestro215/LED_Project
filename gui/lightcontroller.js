let LEDController = class {
    constructor(model, view) {
        this.model = model;
        this.view = view;

        // When something happens in the view, make something happen
        view.addListener((e) => {
            // TODO
            let pix = model.pixels[e.id];
            if (e.action == "click") {
                // If this pixel is already the chosen color, turn it off
                if (pix.r == e.color.r && pix.g == e.color.g && pix.b == e.color.b) {
                    pix.changeColor(0, 0, 0);
                } else {
                    pix.changeColor(e.color.r, e.color.g, e.color.b);
                }
            }
        });
    }
}