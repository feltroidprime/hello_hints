mod oracle;
mod hints_io;

#[cfg(test)]
mod tests {
    use super::oracle::{Response, Request, SqrtOracle};
    use super::hints_io;
    #[test]
    fn sqrt_test() {
        let num = 16;

        let request = Request { n: num };
        let result: Response = SqrtOracle::sqrt(request);
        let res: felt252 = hints_io::parse_felt252(@(result.value));
        println!("res: {res}");
        assert_eq!(res * res, num.into());
    }
}
