use crate::domain::{Entity, GRAVITY};

// Physics methods

fn freefall(t: f64) -> f64 {
    0.5 * GRAVITY * t
}

// Other methods

fn get_cuid() -> String {
    cuid2::create_id()
}

fn get_entity(name: String) -> Entity {
    let result: Entity = Entity {
        name,
        id: get_cuid(),
        pos: [0.0, 0.0],
    };
    result
}

#[macro_export]
macro_rules! create_entity {
    (name) => {};
}
