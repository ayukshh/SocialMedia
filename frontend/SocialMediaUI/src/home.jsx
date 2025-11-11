import React, { useEffect, useState } from "react";
import axios from "axios";

function PostsFeed({ token }) {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = () => {
    axios.get("http://localhost:8000/posts/")
      .then(res => setPosts(res.data))
      .catch(err => console.log(err));
  };

  const handleLike = (postId) => {
    if (!token) return; // only token bearer can like
    axios.post(`http://localhost:8000/likes/${postId}`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(() => fetchPosts())
    .catch(err => console.log(err));
  };

  const handleUnlike = (postId) => {
    if (!token) return;
    axios.delete(`http://localhost:8000/likes/${postId}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(() => fetchPosts())
    .catch(err => console.log(err));
  };

  const [newComment, setNewComment] = useState({});

  const handleComment = (postId) => {
    if (!token || !newComment[postId]) return;
    axios.post(`http://localhost:8000/comments/${postId}`, 
      { text: newComment[postId] }, 
      { headers: { Authorization: `Bearer ${token}` } }
    )
    .then(() => {
      setNewComment({ ...newComment, [postId]: "" });
      fetchPosts();
    })
    .catch(err => console.log(err));
  };

  return (
    <div className="posts-feed">
      <h2>Feed</h2>
      <ul>
        {posts.map(post => (
          <li key={post.id} className="post-item">
            <p><strong>{post.owner_name}</strong></p>
            <p>{post.content}</p>

            <div className="comments-section">
              {post.comments.map(comment => (
                <p key={comment.id}><strong>{comment.user_name}:</strong> {comment.text}</p>
              ))}

              {token && (
                <div className="comment-input">
                  <input
                    value={newComment[post.id] || ""}
                    onChange={e => setNewComment({ ...newComment, [post.id]: e.target.value })}
                    placeholder="Add a comment..."
                  />
                  <button onClick={() => handleComment(post.id)}>Comment</button>
                </div>
              )}
            </div>

            {token && (
              <div className="post-actions">
                {post.liked_by_user
                  ? <button onClick={() => handleUnlike(post.id)}>Unlike</button>
                  : <button onClick={() => handleLike(post.id)}>Like</button>
                }
                <span>{post.likes_count} likes</span>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostsFeed;
