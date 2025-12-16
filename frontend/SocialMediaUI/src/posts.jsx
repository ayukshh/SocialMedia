import { useState } from "react";

function App() {
  const [posts, setPosts] = useState([]);
  const [text, setText] = useState("");
  const [image, setImage] = useState(null);

  // Handle image upload
  const handleImageChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setImage(URL.createObjectURL(e.target.files[0]));
    }
  };

  // Create post
  const handlePost = () => {
    if (!text && !image) return;

    const newPost = {
      id: Date.now(),
      text,
      image,
      liked: false,
      likes: 0,
      comments: []
    };

    setPosts([newPost, ...posts]);
    setText("");
    setImage(null);
  };

  // Like toggle
  const toggleLike = (id) => {
    setPosts(
      posts.map((post) =>
        post.id === id
          ? {
              ...post,
              liked: !post.liked,
              likes: post.liked ? post.likes - 1 : post.likes + 1
            }
          : post
      )
    );
  };

  // Add comment
  const addComment = (id, comment) => {
    if (!comment) return;

    setPosts(
      posts.map((post) =>
        post.id === id
          ? { ...post, comments: [...post.comments, comment] }
          : post
      )
    );
  };

  // Delete post
  const deletePost = (id) => {
    setPosts(posts.filter((post) => post.id !== id));
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h2>Create Post</h2>

      <textarea
        placeholder="What's on your mind?"
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{ width: "100%", marginBottom: 10 }}
      />

      <input type="file" onChange={handleImageChange} />

      <br />
      <button onClick={handlePost} style={{ marginTop: 10 }}>
        Post
      </button>

      <hr />

      {posts.map((post) => (
        <Post
          key={post.id}
          post={post}
          toggleLike={toggleLike}
          addComment={addComment}
          deletePost={deletePost}
        />
      ))}
    </div>
  );
}

// Post component inside same file
function Post({ post, toggleLike, addComment, deletePost }) {
  const [commentText, setCommentText] = useState("");

  return (
    <div style={{ border: "1px solid #ccc", padding: 15, marginBottom: 20 }}>
        <p>Username:{}</p>
      <p>{post.text}</p>

      {post.image && (
        <img
          src={post.image}
          alt="post"
          style={{ width: "100%", marginBottom: 10 }}
        />
      )}

      <button onClick={() => toggleLike(post.id)}>
        {post.liked ? "💖 Unlike" : "🤍 Like"} ({post.likes})
      </button>

      <button
        onClick={() => deletePost(post.id)}
        style={{ marginLeft: 10 }}
      >
        🗑 Delete
      </button>

      <div style={{ marginTop: 10 }}>
        <input
          type="text"
          placeholder="Add a comment..."
          value={commentText}
          onChange={(e) => setCommentText(e.target.value)}
        />
        <button
          onClick={() => {
            addComment(post.id, commentText);
            setCommentText("");
          }}
        >
          Comment
        </button>
      </div>

      {post.comments.map((comment, index) => (
        <p key={index}>💬 {comment}</p>
      ))}
    </div>
  );
}

export default App;



//made the post and list them using .map
//so basically i made posts in array [post1, post2]
//and list it 
//think of it like making a to-do list