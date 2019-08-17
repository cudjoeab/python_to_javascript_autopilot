function getNewCar() {
    return {
    'city': 'Toronto',
    'passengers': 0,
    'gas': 100,
    };
};

function addCar(cars, new_car) {
    cars.push(new_car);
    return `Adding new car to fleet. Fleet size is now ${cars.length}.`;
}; 

function pickUpPassenger(car) {
    car['passengers'] += 1
    car['gas'] -= 10
    return `Picked up passenger. Car now has ${car['passengers']} passengers.`
}; 

function getDestination(car) {
    if (car['city'] === 'Toronto') {
        return 'Missisauga'; 
    } else if (car['city'] === 'Missisauga') {
        return 'London'; 
    } else if (car['city'] === 'London') {
        return 'Toronto'; 
    } else {
        return 'Destination not found.'
    }
}

function fillUpGas(car) {
    let old_gas = car['gas']; 
    let car['gas'] = 100;
    return `Filled up to ${car['gas']} on gas from ${old_gas}.`; 
}

function getGasDisplay(gas_amount) {
    return `${gas_amount}`; 
}

function drive (car, city_distance) {
    if (car['gas'] < city_distance) {
        return fill_up_gas(car); 
    } else {
        car['city'] = get_destination(car)
        car['gas'] -= city_distance
        return `Drove to ${car['city']}. Remaining gas: ${car['gas']}.`;
}

function dropOffPassengers(car) {
     previous_passengers = car['passengers'];
     car['passengers'] = 0; 
     return `Dropped off ${previous_passengers}.`
}

function act(car) {
    let distanceBetweenCities = 50

    if (car['gas'] < 20) {
         return fillUpGas(car); 
    } else if (car['passengers'] < 3) {
        return pickUpPassenger(car); 
    } else {
        if (car['gas'] < distanceBetweenCities) {
            return fillUpGas(car); 
        }
    }

    let drove_to = drive(car, distance_between_cities)
    let passengers_dropped = dropOffPassengers(car)
    return `${drove_to} ${passengers_dropped}` 
}

function commandFleet(cars) {
    let i = 1 
    for (let car = 0; index < cars.length; index ++) {
        action = act(cars[index]);
        console.log(`Car ${i}: ${action} `);
        i += 1
    }
    console.log('---')
}

function addOneCarPerDay(cars, num_days) {
    for (let i = 0; i < num_days; i++){
        new_car = getNewCar();
        console.log(add_car(cars, new_car));
        commandFleet(cars);
    }
}

var cars = [];
addOneCarPerDay(cars, 10);
