use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn part_1() {
    let lines = lines_from_file("src/input.txt");
    let expenses: Vec<i32> = lines
        .iter()
        .map(
            |l| l.parse::<i32>().unwrap()
        ).collect();
    let year: i32 = 2020;
    let mut target_expense: i32 = 0;
    let mut target_diff: i32 = 0;

    for expense in expenses.iter() {
        let diff = year - expense;

        if expenses.contains(&diff) {
            target_expense = *expense;
            target_diff = diff;
            break;
        }
    }

    println!("expense lines: {} x {} = {}", target_expense, target_diff, target_expense * target_diff);
}

fn main() {
    part_1();
}
