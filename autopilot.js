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


