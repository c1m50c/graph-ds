use super::Graph;


#[test]
fn verticies() {
    let mut graph = Graph::new();

    graph.add_vertex(0);
    graph.add_vertex(1);
    graph.add_vertex(2);
    assert_eq!(graph.verticies(), 3);
}


#[test]
fn edges() {
    let mut graph = Graph::new();

    graph.add_vertex(0); graph.add_vertex(1);
    graph.add_edge(&mut 0, &mut 1);
    graph.add_edge(&mut 1, &mut 0);
    assert_eq!(graph.edges(), 2);
}


#[test]
fn add_vertex() {
    let mut graph = Graph::new();

    graph.add_vertex(0); graph.add_vertex(1);
    assert_eq!(graph.verticies(), 2);
}


#[test]
fn remove_vertex() {
    let mut graph = Graph::new();

    graph.add_vertex(0); graph.add_vertex(1);
    graph.remove_vertex(&0);
    assert_eq!(graph.verticies(), 1);
}


#[test]
fn add_edge() {
    let mut graph = Graph::new();

    graph.add_vertex(4); graph.add_vertex(2);
    graph.add_edge(&mut 4, &mut 2);
    assert_eq!(graph.edges(), 1);
}


#[test]
#[ignore] // TODO: Remove ignore tag when function is fixed.
fn remove_edge() {
    let mut graph = Graph::new();

    graph.add_vertex(3); graph.add_vertex(0);
    graph.add_edge(&mut 3, &mut 0);
    graph.add_edge(&mut 0, &mut 3);
    assert_eq!(graph.edges(), 2);

    println!("PreR {:?}", graph.adj_list);
    graph.remove_edge(&mut 3, &mut 0);
    println!("R {:?}", graph.adj_list);
    assert_eq!(graph.edges(), 1);
}