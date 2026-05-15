mod domain;
mod helpers;

use std::{thread::sleep, time::Duration};

use crate::domain::{TICK, World};

fn main() {
    println!("Hello, big dog!");

    println!("Defining tick duration");
    let tick_dur = Duration::new(TICK, 0);

    println!("Creating new world");
    let mut world = World {
        time: 0,
        entities: vec![],
    };

    println!("Creating new spherical cow");
    println!("Adding entities to world");
    // world.entities.push(cow);

    println!("Beginning loop");
    loop {
        println!("Current tick {}", world.time);

        println!("Doing things to the following entities:");
        // world.entities.iter().for_each(|e| println!("{ e.name }"));

        sleep(tick_dur);
        world.time += TICK;
    }
}
