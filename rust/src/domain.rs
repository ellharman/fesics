pub const GRAVITY: f64 = 9.80665;
pub const TICK: u64 = 1;

pub struct World {
    pub time: u64,
    pub entities: Vec<Entity>,
}

// TODO impl with new()
pub struct Entity {
    pub id: String,
    pub name: String,
    pub pos: [f64; 2],
}
