const Effect = class {
    constructor(name) {
        this.name = name;
        this.setDefault();
    }

    setDefault() {
        this.begin = 0;
        this.end = 300;
        this.bc = 1;
    }
    getOptions() {
        // Create a wrapper for all of this effect's options
        const options_wrapper = document.createElement('div');
        options_wrapper.setAttribute('class', '');
        options_wrapper.innerHTML = `<h6>${this.name}</h6>`;

        // Create some nice looking input fields
        // // Begin
        // const begin_wrapper = document.createElement('div');
        // begin_wrapper.setAttribute('class', 'input-group mb-3');
        // const begin_group_prepend = document.createElement('div');
        // begin_group_prepend.setAttribute('class', 'input-group-prepend');
        // begin_wrapper.append(begin_group_prepend);
        // const begin_label = document.createElement('span');
        // begin_label.setAttribute('class', 'input-group-text');
        // begin_label.innerText = 'Begin';
        // begin_group_prepend.append(begin_label);
        // const begin_input = document.createElement('input');
        // begin_input.setAttribute('class', 'form-control');
        // begin_input.type = 'number';
        // begin_input.value = this.begin;
        // begin_input.min = 0;
        // begin_input.max = 300;
        // begin_wrapper.append(begin_input);
        // options_wrapper.append(begin_wrapper);
        // // End
        // const end_wrapper = document.createElement('div');
        // end_wrapper.setAttribute('class', 'input-group mb-3');
        // const end_group_prepend = document.createElement('div');
        // end_group_prepend.setAttribute('class', 'input-group-prepend');
        // end_wrapper.append(end_group_prepend);
        // const end_label = document.createElement('span');
        // end_label.setAttribute('class', 'input-group-text');
        // end_label.innerText = 'End';
        // end_group_prepend.append(end_label);
        // const end_input = document.createElement('input');
        // end_input.setAttribute('class', 'form-control');
        // end_input.type = 'number';
        // end_input.value = this.end;
        // end_input.min = 0;
        // end_input.max = 300;
        // end_wrapper.append(end_input);
        // options_wrapper.append(end_wrapper);

        // BC
        const bc_wrapper = `<div class="input-group mb-3">\
                                <div class="input-group-prepend">\
                                    <span class="input-group-text">Brightness</span>\
                                </div>
                                <input class="form-control" type="number" value="${this.bc}" min="0" max="1" step="0.1">\
                            </div>`;
        // const bc_wrapper = document.createElement('div');
        // bc_wrapper.setAttribute('class', 'input-group mb-3');
        // const bc_group_prepend = document.createElement('div');
        // bc_group_prepend.setAttribute('class', 'input-group-prepend');
        // bc_wrapper.append(bc_group_prepend);
        // const bc_label = document.createElement('span');
        // bc_label.setAttribute('class', 'input-group-text');
        // bc_label.innerText = 'Brightness';
        // bc_group_prepend.append(bc_label);
        // const bc_input = document.createElement('input');
        // bc_input.setAttribute('class', 'form-control');
        // bc_input.type = 'number';
        // bc_input.value = this.bc;
        // bc_input.min = 0;
        // bc_input.max = 1;
        // bc_input.step = 0.1;
        // bc_wrapper.append(bc_input);
        // options_wrapper.append(bc_wrapper);
        options_wrapper.innerHTML += bc_wrapper;

        return options_wrapper;
    }
    // setBegin(begin) { this.begin = begin; }
    // setEnd(end) { this.end = end; }
    // setBC(bc) { this.bc = bc; }
}

const Fill = class extends Effect {
    constructor() {
        super('Fill');
    }

    setDefault() {
        super.setDefault();
        this.color = { r: 255, g: 255, b: 255 }
    }

    getOptions() {
        const options_wrapper = super.getOptions();

        // Color Selector
        const color_wrapper = document.createElement('div');
        color_wrapper.setAttribute('class', 'input-group mb-3');
        color_wrapper.innerHTML =   `<div class="input-group-prepend">\
                                        <span class="input-group-text">Color</span>\
                                    </div>
                                    <input class="form-control" type="color" value="${this.color}">`;
        // const color_wrapper = document.createElement('div');
        // color_wrapper.setAttribute('class', 'input-group mb-3');
        // const color_group_prepend = document.createElement('div');
        // color_group_prepend.setAttribute('class', 'input-group-prepend');
        // color_wrapper.append(color_group_prepend);
        // const color_label = document.createElement('span');
        // color_label.setAttribute('class', 'input-group-text');
        // color_label.innerText = 'Color';
        // color_group_prepend.append(color_label);
        // const color_input = document.createElement('input');
        // color_input.setAttribute('class', 'form-control');
        // color_input.type = 'color';
        // color_input.value = this.color;
        // color_wrapper.append(color_input);

        options_wrapper.insertBefore(color_wrapper, options_wrapper.childNodes[1]);
        return options_wrapper;
    }
    // setColor(color) { this.color = color; }
}

const Empty = class extends Effect {
    constructor() {
        super('Empty');
    }

    setDefault() {
        super.setDefault();
        this.color = { r: 0, g: 0, b: 0 }
    }
}

const Meteor = class extends Effect {
    constructor() {
        super('Meteor');
    }

    setDefault() {
        super.setDefault();
        this.color = { r: 255, g: 255, b: 255 };
        this.size = 1;
        this.trail_decay = 80;
        this.random_decay = true;
        this.speed = 1;
    }

    getOptions() {
        const options_wrapper = super.getOptions();

        // Color Selector
        const color_wrapper = document.createElement('div');
        color_wrapper.setAttribute('class', 'input-group mb-3');
        color_wrapper.innerHTML =   `<div class="input-group-prepend">\
                                        <span class="input-group-text">Color</span>\
                                    </div>
                                    <input class="form-control" type="color" value="${this.color}">`;

        options_wrapper.insertBefore(color_wrapper, options_wrapper.childNodes[1]);

        // Size Selector
        const size_wrapper = document.createElement('div');
        size_wrapper.setAttribute('class', 'input-group mb-3');
        size_wrapper.innerHTML =   `<div class="input-group-prepend">\
                                        <span class="input-group-text">Size</span>\
                                    </div>
                                    <input class="form-control" type="number" value="${this.size}" min="1">`;

        options_wrapper.insertBefore(size_wrapper, options_wrapper.childNodes[2]);

        // Trail Decay Selector
        const trail_decay_wrapper = document.createElement('div');
        trail_decay_wrapper.setAttribute('class', 'input-group mb-3');
        trail_decay_wrapper.innerHTML = `<div class="input-group-prepend">\
                                            <span class="input-group-text">Trail Decay</span>\
                                        </div>
                                        <input class="form-control" type="number" value="${this.trail_decay}">`;

        options_wrapper.insertBefore(trail_decay_wrapper, options_wrapper.childNodes[3]);

        // Random Decay Selector
        const random_wrapper = document.createElement('div');
        random_wrapper.setAttribute('class', 'input-group mb-3');
        random_wrapper.innerHTML =   `<div class="input-group-prepend">\
                                        <span class="input-group-text">Random Decay</span>\
                                    </div>
                                    <input class="form-control" type="checkbox" checked>`;

        options_wrapper.insertBefore(random_wrapper, options_wrapper.childNodes[4]);

        // Speed Selector
        const speed_wrapper = document.createElement('div');
        speed_wrapper.setAttribute('class', 'input-group mb-3');
        speed_wrapper.innerHTML =   `<div class="input-group-prepend">\
                                        <span class="input-group-text">Speed</span>\
                                    </div>
                                    <input class="form-control" type="number" value="${this.speed}">`;

        options_wrapper.insertBefore(speed_wrapper, options_wrapper.childNodes[5]);
        return options_wrapper;
    }
    // setColor(color) { this.color = color; }
}