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
        options_wrapper.innerText = this.name;

        // Create some nice looking input fields
        // Begin
        const begin_wrapper = document.createElement('div');
        begin_wrapper.setAttribute('class', 'input-group mb-3');
        const begin_group_prepend = document.createElement('div');
        begin_group_prepend.setAttribute('class', 'input-group-prepend');
        begin_wrapper.append(begin_group_prepend);
        const begin_label = document.createElement('span');
        begin_label.setAttribute('class', 'input-group-text');
        begin_label.innerText = 'Begin';
        begin_group_prepend.append(begin_label);
        const begin_input = document.createElement('input');
        begin_input.setAttribute('class', 'form-control');
        begin_input.type = 'number';
        begin_input.value = this.begin;
        begin_input.min = 0;
        begin_input.max = 300;
        begin_wrapper.append(begin_input);
        options_wrapper.append(begin_wrapper);
        // End
        const end_wrapper = document.createElement('div');
        end_wrapper.setAttribute('class', 'input-group mb-3');
        const end_group_prepend = document.createElement('div');
        end_group_prepend.setAttribute('class', 'input-group-prepend');
        end_wrapper.append(end_group_prepend);
        const end_label = document.createElement('span');
        end_label.setAttribute('class', 'input-group-text');
        end_label.innerText = 'End';
        end_group_prepend.append(end_label);
        const end_input = document.createElement('input');
        end_input.setAttribute('class', 'form-control');
        end_input.type = 'number';
        end_input.value = this.end;
        end_input.min = 0;
        end_input.max = 300;
        end_wrapper.append(end_input);
        options_wrapper.append(end_wrapper);
        // BC
        const bc_wrapper = document.createElement('div');
        bc_wrapper.setAttribute('class', 'input-group mb-3');
        const bc_group_prepend = document.createElement('div');
        bc_group_prepend.setAttribute('class', 'input-group-prepend');
        bc_wrapper.append(bc_group_prepend);
        const bc_label = document.createElement('span');
        bc_label.setAttribute('class', 'input-group-text');
        bc_label.innerText = 'Brightness';
        bc_group_prepend.append(bc_label);
        const bc_input = document.createElement('input');
        bc_input.setAttribute('class', 'form-control');
        bc_input.type = 'number';
        bc_input.value = this.bc;
        bc_input.min = 0;
        bc_input.max = 1;
        bc_input.step = 0.1;
        bc_wrapper.append(bc_input);
        options_wrapper.append(bc_wrapper);

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
    // setColor(color) { this.color = color }
}

const Meteor = class extends Effect {
    constructor() {
        super('Meteor');
    }

    setDefault() {
        super.setDefault();
        this.color = { r: 255, g: 255, b: 255 };
        this.size = 1;;
        this.trail_decay = 80;;
        this.random_decay = true;;
        this.speed = 1;;
    }
    // setColor(color) { this.color = color }
}