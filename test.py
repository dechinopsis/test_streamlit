import streamlit as st
import asyncio


async def async_job():
    st.text("Async job is running...")

    batches = 3
    for i in range(batches):
        await asyncio.sleep(1)
        st.text(f"Executing batch {i+1}/{batches}...")
    st.text("Async job is finished!")


def main():
    st.title("Async Streamlit App")

    asyncio.run(async_job())

    if st.button("Next Step"):
        st.title("Next Step Screen")
        st.text("You pressed the 'Next Step' button!")


if __name__ == "__main__":
    main()
