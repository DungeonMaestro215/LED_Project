const View = class {
    effect;
    effects;

    constructor() {
        // All available effects
        this.effects = [new Empty(), new Fill(), new Strobe(), new Flash(), new Meteor()];
        // console.log(this.effects);

        this.populateButtons();
    }

    // Create necessary buttons for all available effects
    populateButtons() {
        const quick_effects = document.getElementById('quick-effects');
        for(const effect of this.effects) {
            // console.log(effect);
            const effect_butt = document.createElement('button');
            effect_butt.setAttribute('class', 'btn btn-secondary');
            effect_butt.innerText = effect.name;
            effect_butt.addEventListener('click', () => {
                this.effect = effect;
                const options_div = document.getElementById('quick-effect-options');
                options_div.innerHTML = '';
                options_div.append(effect.getOptions());
                this.bindSettings();
            });

            quick_effects.append(effect_butt);
        }
    }

    // Bind options buttons to the current effect object.
    // Changes in these settings will be saved in their corresponding objects
    bindSettings() {
        const settings = document.getElementsByClassName('setting');
        for (const setting of settings) {
            setting.addEventListener('input', (e) => {
                const setting_name = e.target.getAttribute('data-setting');
                this.effect[setting_name] = e.target.value;
                console.log(setting_name);
            });
        }
    }
}