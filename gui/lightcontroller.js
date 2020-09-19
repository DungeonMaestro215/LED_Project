let LEDController = class {
    constructor(model, view) {
        this.model = model;
        this.view = view;

        let xhttp = new XMLHttpRequest();
        // When something happens in the view, make something happen
        view.addListener((e) => {
            // TODO
            let pix = model.pixels[e.id];
            if (e.action == "click") {
                // If this pixel is already the chosen color, turn it off
                if (pix.r == e.color.r && pix.g == e.color.g && pix.b == e.color.b) {
                    xhttp.open("GET", `main.php?idx=${e.id}&r=0&g=0&b=0`, true);
                    xhttp.send();
                    pix.changeColor(0, 0, 0);
                } else {
                    xhttp.open("GET", `main.php?idx=${e.id}&r=${e.color.r}&g=${e.color.g}&b=${e.color.b}`, true);
                    xhttp.send();
                    pix.changeColor(e.color.r, e.color.g, e.color.b);
                }
            }
        });
    }
}
