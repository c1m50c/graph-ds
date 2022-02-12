//! Module containing a [`Graph`] implemented with an *adjacency list*.
//! This type of [`Graph`] scales much better than the usual alternative of an *adjacency matrix*, which requires much more space.
//! The *adjacency list* is implemented with a [`HashMap`] containing a type (`T`) and a [`HashSet`] of [`NonNull`] pointers to keys.
//! The pointers represent the edges of the [`Graph`] while the keys represent the verticies.


#[cfg(test)]
mod tests;

use std::collections::{HashMap as Map, HashSet as Set};
use core::ptr::NonNull;
use core::hash::Hash;
use core::cmp::Eq;


pub struct Graph<T> {
    adj_list: Map<T, Set<NonNull<T>>>,
}


impl<T> Graph<T> {
    #[inline]
    pub fn new() -> Self {
        return Self {
            adj_list: Map::new(),
        };
    }

    #[inline]
    pub fn verticies(&self) -> usize {
        return self.adj_list.len();
    }

    #[inline]
    pub fn edges(&self) -> usize {
        let mut result = 0;
        
        for (_, set) in &self.adj_list {
            result += set.len();
        }
        
        return result;
    }
}


impl<T: Eq + Hash> Graph<T> {
    /// Creates a new `vertex` within the [`Graph`].
    #[inline]
    pub fn add_vertex(&mut self, vertex: T) {
        self.adj_list.insert(
            vertex, Set::new()
        );
    }

    /// Removes the specified `vertex` from the [`Graph`].
    #[inline]
    pub fn remove_vertex(&mut self, vertex: &T) {
        self.adj_list.remove(vertex);
    }

    /// Creates an edge from `vertex_a` connecting to `vertex_b`.
    #[inline]
    pub fn add_edge(&mut self, vertex_a: &mut T, vertex_b: &mut T) {
        match self.adj_list.get_mut(vertex_a) {
            Some(set) => {
                set.insert(NonNull::from(vertex_b));
            },

            _ => {  },
        }
    }

    /// Removes the edge from `vertex_a` connecting to `vertex_b`.
    #[inline]
    pub fn remove_edge(&mut self, vertex_a: &mut T, vertex_b: &mut T) {
        // FIXME: Does not remove the edge even when reference is proper.
        match self.adj_list.get_mut(vertex_a) {
            Some(set) => {
                set.remove(&NonNull::from(vertex_b));
            },

            _ => {  },
        }
    }
}