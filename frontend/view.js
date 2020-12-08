const View = class {
    constructor() {
        // All available effects
        this.effects = [new Empty(), new Fill(), new Meteor()];
        console.log(this.effects);

        this.populateButtons();
    }

    // Create necessary buttons for all available effects
    populateButtons() {
        const quick_effects = document.getElementById('quick-effects');
        for(const effect of this.effects) {
            console.log(effect);
            const effect_butt = document.createElement('button');
            effect_butt.setAttribute('class', 'btn btn-secondary');
            effect_butt.innerText = effect.name;
            effect_butt.addEventListener('click', () => {
                const options_div = document.getElementById('quick-effect-options');
                options_div.innerHTML = '';
                options_div.append(effect.getOptions());
            });

            quick_effects.append(effect_butt);
        }
    }
}