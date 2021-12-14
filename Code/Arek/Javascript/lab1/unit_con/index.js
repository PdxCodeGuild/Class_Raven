
//feet, meters, inches, miles, kilometers, yards


var distance = prompt("What is the distance? ")
var startUnit = prompt("What is the starting unit? ")
var endUnit = prompt("What is the ending unit? ")


let units = {
    meters: {
        'inches': distance * 39.37,
        'feet': distance * 3.281,
        'meters': distance * 1,
        'yards': distance * 1.094,
        'kilometers': distance * 1000,
        'miles': distance / 1609
    },
    feet: {
        'inches': distance * 12,
        'feet': distance * 1,
        'meters': distance / 3.281,
        'yards': distance / 3,
        'kilometers': distance / 3281,
        'miles': distance / 5280


    },
    inches: {
        'inches': distance * 1,
        'feet': distance / 12,
        'meters': distance / 39.37,
        'yards': distance / 36,
        'kilometers': distance / 39370,
        'miles': distance / 63360
    },
    yards: {
        'inches': distance * 36,
        'feet': distance * 3,
        'meters': distance / 1.094,
        'yards': distance * 1,
        'kilometers': distance / 1094,
        'miles': distance / 1760
    },
    miles: {
        'inches': distance * 63360,
        'feet': distance * 5280,
        'meters': distance * 1609,
        'yards': distance * 1760,
        'kilometers': distance * 1.609,
        'miles': distance * 1
    },
    kilometers: {
        'inches': distance * 39370,
        'feet': distance * 3281,
        'meters': distance * 1000,
        'yards': distance * 1094,
        'kilometers': distance * 1,
        'miles': distance / 1.609
    }
    




}



console.log(`${distance} ${startUnit} is equal to ${units[startUnit][endUnit]} ${endUnit}(s)`)