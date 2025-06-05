console.log('disable-same-city.js loaded');

document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener('change', () => {
        const selectedDeparture = document.querySelector('input[name="departure_city"]:checked')?.value;
        const selectedArrival = document.querySelector('input[name="arrival_city"]:checked')?.value;

        // Re-enable all options first
        document.querySelectorAll('input[name="departure_city"]').forEach(r => r.disabled = false);
        document.querySelectorAll('input[name="arrival_city"]').forEach(r => r.disabled = false);

        // Disable arrival option if it matches selected departure
        if (selectedDeparture) {
            document.querySelectorAll('input[name="arrival_city"]').forEach(r => {
                if (r.value === selectedDeparture) {
                    r.disabled = true;
                    if (r.checked) r.checked = false;
                }
            });
        }

        // Disable departure option if it matches selected arrival
        if (selectedArrival) {
            document.querySelectorAll('input[name="departure_city"]').forEach(r => {
                if (r.value === selectedArrival) {
                    r.disabled = true;
                    if (r.checked) r.checked = false;
                }
            });
        }
    });
});

